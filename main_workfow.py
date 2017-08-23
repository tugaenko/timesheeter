from constants import *
from timesheet_operations import *
from hg_operations import *

def main_workflow():
	chunk_list = log_parser(hg_log_reader())
	time1, is_new_day =  get_start_time() # new_day adds empty line

	if is_new_day:
		timesheet_writer("\n")
	
	for el in chunk_list:
		timesheet_writer(timesheet_string_formater(el, time1))
		time1 = el.get_datetime().strftime("%H:%M")

main_workflow()


# print timesheet_line_to_dt()
# print get_start_time()












