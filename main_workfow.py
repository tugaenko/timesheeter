from constants import *
from timesheet_operations import *
from hg_operations import *

def main_workflow():
	hg_log = hg_log_reader(MOCK_FLAG)
	log_chunks_list = log_parser(hg_log)
	time1, is_new_day =  get_start_time() # new_day adds empty line

	trim_short_lines()

	if is_new_day:
		timesheet_writer("")

	for el in log_chunks_list:
		temp_time = el.get_datetime()
		if temp_time.time() < time1:
			timesheet_writer(timesheet_string_formater(el, time1))
			time1 = temp_time.strftime("%H:%M")

main_workflow()



# print timesheet_line_to_dt()
# print get_start_time()












