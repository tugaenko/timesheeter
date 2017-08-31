from constants import *
from timesheet_operations import *
from hg_operations import *

def main_workflow():
	hg_log = hg_log_reader()
	log_chunks_list = log_parser(hg_log)
	time1, is_new_day =  get_start_time() # new_day adds empty line

	trim_short_lines()
	
	if is_new_day:
		timesheet_writer("")

	
	for el in log_chunks_list:
		timesheet_writer(timesheet_string_formater(el, time1))
		time1 = el.get_datetime().strftime("%H:%M")

main_workflow()


# print timesheet_line_to_dt()
# print get_start_time()












