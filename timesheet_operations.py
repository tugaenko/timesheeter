from constants import *
from datetime import datetime

def get_last_timesheet_line():
	with open(TIMESHEET_FILE) as file:
		lines = file.readlines()
	for line in lines[ : -LINES_TO_REMOVE : -1]:
		if len(line) > MIN_TIMESHEET_STRING_LEN:
			return line
			break
	raise ValueError("the last 30 strings in timesheet are too short")

def __get_expicit_start_time():
	with open(TIMESHEET_FILE) as file:
		lines = file.readlines()
	for line in lines[ : -LINES_TO_REMOVE : -1]:
		clean_line = line.strip()
		if len(clean_line) == 4 and clean_line.isdigit():
			# start_time_dt = datetime.strptime(line, "%H%M")
			return clean_line[:2] + ":" + clean_line[2:]
		elif len(line) > SHORT_LINE:
			break

def timesheet_line_to_dt():
	last_line = get_last_timesheet_line()
	str_dt = last_line[:10] + " " + last_line[17:22]
	dt = datetime.strptime(str_dt, "%Y-%m-%d %H:%M")
	return dt

# returns tuple: (time_string, is_new_day_boolean_flag)
def get_start_time(): 
	timesheet_dt = timesheet_line_to_dt()
	if timesheet_dt.date() < datetime.now().date():
		explicit_start_time = __get_expicit_start_time()
		if explicit_start_time:
			return explicit_start_time, True
		else:
			return ARRIVAL, True
	return timesheet_dt.strftime("%H:%M"), False

def timesheet_writer(timesheet_string):
	fh = open(TIMESHEET_FILE, 'a')
	fh.write(timesheet_string + '\n')
	fh.close()

def trim_blank_lines(): 
	fh = open(TIMESHEET_FILE, "r+")
	empty_lines_counter = 0
	lines = fh.readlines()
	for line in lines[:-LINES_TO_REMOVE:-1]:
		if line.strip() == "":
			empty_lines_counter += 1
		elif empty_lines_counter > 0:
			fh.close()
			fh = open(TIMESHEET_FILE, "w")
			fh.writelines(lines[:-empty_lines_counter ])
			# fh.write(line[:-1])
			fh.close()
			return
		else:
			fh.close()
			return
	raise ValueError("the last {0} strings in timesheet are all blank".format(LINES_TO_REMOVE))

def trim_short_lines(): 
	fh = open(TIMESHEET_FILE, "r+")
	short_lines_counter = 0
	lines = fh.readlines()
	for line in lines[:-LINES_TO_REMOVE:-1]:
		if len(line) <= SHORT_LINE and line.strip() != "#eom":
			short_lines_counter += 1
		elif short_lines_counter > 0:
			fh.close()
			fh = open(TIMESHEET_FILE, "w")
			fh.writelines(lines[:-short_lines_counter])
			# fh.write(line[:-1])
			fh.close()
			return
		else:
			fh.close()
			return
	raise ValueError("the last {0} strings in timesheet are too short".format(LINES_TO_REMOVE))

# timesheet_writer("trololo")
# trim_blank_lines()

# print __get_expicit_start_time()
