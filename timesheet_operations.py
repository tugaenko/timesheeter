from constants import *
from datetime import datetime

def get_last_timesheet_line():
	with open(TIMESHEET_FILE) as file:
		lines = file.readlines()
	file.close()
	for line in lines[:-30:-1]:
		if len(line) > 32:
			return line
			break
	raise ValueError("the last 30 strings in timesheet are too short")

def timesheet_line_to_dt():
	last_line = get_last_timesheet_line()
	str_dt = last_line[:10] + " " + last_line[17:22]
	dt = datetime.strptime(str_dt, "%Y-%m-%d %H:%M")
	return dt

def get_start_time():
	timesheet_dt = timesheet_line_to_dt()
	if timesheet_dt.date() < datetime.now().date():
		return ARRIVAL, True
	return timesheet_dt.strftime("%H:%M"), False

def timesheet_writer(timesheet_string):
	fh = open(TIMESHEET_FILE, 'a')
	fh.write(timesheet_string + '\n')
	fh.close()

def remove_blank_lines():
	fh = open(TIMESHEET_FILE, "r+")
	empty_lines_counter = 0
	lines = fh.readlines()
	for line in lines[:-30:-1]:
		if line.strip() == "":
			empty_lines_counter += 1
			print empty_lines_counter
		elif empty_lines_counter > 0:
			fh.close()
			fh = open(TIMESHEET_FILE, "w")
			fh.writelines(lines[:-empty_lines_counter - 1 ])
			fh.write(line[:-1])
			break
		else:
			print "break line: " + line
			break
	fh.close()
	# raise ValueError("the last 30 strings in timesheet are too short")
# timesheet_writer("trololo")
remove_blank_lines()
