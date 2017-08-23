from datetime import datetime
from subprocess import *

from constants import *
from log_mock import *

class log_element:
	def	__init__(self, branch, date, text):
		self.branch = branch
		self.date = date
		self.text = text
	def get_branch(self):
		return self.branch
	def get_datetime(self):
		return self.date
	def get_text(self):
		return self.text
	def __str__(self):
		return str(self.date) + " " + self.branch + " " + self.text

def timesheet_string_formater(element, time1):
	dt = element.get_datetime()
	branch = branch_formater(element.get_branch())
	text = element.get_text()
	date = dt.date().isoformat()
	time1 = time1
	time2 = dt.strftime("%H:%M")
	string_list = [date, time1, time2, QUEUE, branch, '"' + text + '"']
	return ",".join(string_list)

def hg_log_reader():
    #hg_log_string = check_output(["hg", "log", "-u", USER, "-l10"], cwd = "/home/atugaenko/userver")
    return log_output()

def hg_branch_reader():
    # hg_branch_string = check_output(["hg", "branch"], cwd = "/home/atugaenko/userver")
    return "RT123456"
    
def log_parser(log_string):
	chunk_list = list()
	log_list = log_string.split("\n\n")
	for log_chunk in log_list:
		branch, date, text = None, None, None
		chunk_strings = log_chunk.split("\n")
		for string in chunk_strings:
			string_list = string.split(":", 1)
			if string_list[0] == "branch":
				branch =  string_list[1].lstrip()
			if string_list[0] == "date":
				date = string_list[1].lstrip()
			if string_list[0] == "summary":
				text = string_list[1].lstrip()
		if branch and date and text:
			dt = datetime.strptime(date[:-6], "%a %b %d %H:%M:%S %Y") # cut unsupported %z
			if dt.date() < datetime.now().date():
				break
			log_el = log_element(branch, dt, text)
			chunk_list.insert(0, (log_el))
	return chunk_list

def branch_formater(name):
	if name[0:2] == "RT":
		return name[0:2] + ":" + name[2:8]
	else:
		return name
