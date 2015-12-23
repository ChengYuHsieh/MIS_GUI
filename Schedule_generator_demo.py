import time
import random
import sys

global TIME_PERIOD
TIME_PERIOD = 96
global CLASS_TYPE
CLASS_TYPE = 10
global skill_scale
global multiskill_scale
global wd_upperBound
wd_upperBound = 0
global wd_lowerBound
wd_lowerBound = 0
global ws_upperBound
ws_upperBound = 2	#200
global ws_lowerBound
ws_lowerBound = 0

def set_generator(f):
	#Set I(Time period)
	f.write(str(TIME_PERIOD) + "\n\n")

	#Set S(Single skill)
	f.write(str(skill_scale) + "\n\n")

	#Set M(Multi skill)
	f.write(str(multiskill_scale) + "\n\n")

	#Set C(Class type)
	f.write(str(CLASS_TYPE) + "\n\n")


def param_generator(f):
	#param d(Demand of each skill at each time)
	for i in range(skill_scale):
		for j in range(TIME_PERIOD):
			ran = random.randint(wd_lowerBound, wd_upperBound)
			if j != 0:
				f.write(" ")
			f.write(str(ran))
		f.write("\n")
	f.write("\n")

	#param ct(read class type file)
	index = 0
	for i in range(CLASS_TYPE):
		for j in range(TIME_PERIOD):
			ran = random.randint(0, 1)
			if j != 0:
				f.write(" ")
			f.write(str(ran))
		f.write("\n")
		index = index + 1
	f.write("\n")
	# index = 0
	# with open("class_type.txt", "r") as r:
	# 	for line in r:
	# 		for j in range(len(line) - 1):
	# 			if j != 0:
	# 				f.write(" ")
	# 			f.write(line[j])
	# 		f.write("\n")
	# 		index = index + 1
	# 	f.write("\n")

	#param mos(What skill compose a multi skill)
	for i in range(multiskill_scale):
		for j in range(skill_scale):
			ran = random.randint(0, 1)
			if j != 0:
				f.write(" ")
			f.write(str(ran))
		f.write("\n")
	f.write("\n")

	#param ws(Worker num with single skill)
	for i in range(skill_scale):
		ran = random.randint(ws_lowerBound, ws_upperBound)
		if i != 0:
			f.write(" ")
		f.write(str(ran))
	f.write("\n\n")

	#param wm(Worker num with multi skill)
	for i in range(multiskill_scale):
		ran = random.randint(ws_lowerBound, ws_upperBound)
		if i != 0:
			f.write(" ")
		f.write(str(ran))
	f.write("\n\n")
	

#generate data with assign factor
def main(s_scale, m_scale, d_scale):
	global skill_scale
	global multiskill_scale
	global wd_upperBound
	global single_skill_dis
	global multi_skill_dis
	skill_scale = s_scale
	multiskill_scale = m_scale
	wd_upperBound = d_scale
	#file f for lagrangian algo
	with open("inputForLag.txt", "w") as f:
		set_generator(f)
		param_generator(f)

if __name__=="__main__":
	main()