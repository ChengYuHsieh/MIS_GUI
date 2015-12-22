import time
import random
import sys
from datetime import *

global TIME_PERIOD
TIME_PERIOD = 96
global TERMINAL
TERMINAL = 2
global GATE
GATE = 1
global GATE_MOVING
GATE_MOVING = 1
global TERMINAL_MOVING
TERMINAL_MOVING = 1
global REST_FIRST
REST_FIRST = 3
global worker_scale 
global duty_scale
global group_scale
global skill_scale
global demand_scale
global demand_upperBound
global PIORITY
PIORITY = 6
global D
D = 3
global CLASS_TYPE
CLASS_TYPE = 228
global date
date = date.today()

global Output
Output = {"dutyList" : [], "empList" : [], "dutyNum" : 0, "empNum" : 0, "priority" : {}}

def param_generator(f):
	Output["dutyList"] = []
	Output["empList"] = []
	start_duty = {}
	time = {}
	demandSlot = {}
	terminal_duty = {}
	priority = {}
	skill_duty = {}
	start_employ = {}
	terminal_employ = {}
	empSlot = {} #Class time array 96
	skill_emply = {} #skill list

	#Duty demand
	for i in range(duty_scale):
		duty = []
		day = 48
		upper = 6
		ran1 = random.randint(0, 47)
		start_duty[i] = ran1 * 2
		for j in range(ran1):
			duty.append(0)
			duty.append(0)
		if day - ran1 < 6:
			upper = day - ran1
		ran2 = random.randint(1, upper)
		time[i] = ran2 * 2
		ran_demand = random.randint(1, demand_scale)
		for j in range(ran2):
			duty.append(ran_demand)
			duty.append(ran_demand)
		if day - ran1 - ran2 > 0:
			for j in range(day - ran1 -ran2):
				duty.append(0)
				duty.append(0)
		demandSlot[i] = duty

	#param ct(read class type file)
	index = 0
	classType = {}
	with open("class_type_day.txt", "r") as r:
		for line in r:
			classType[index] = []
			for j in range(len(line) - 1):
				classType[index].append(int(line[j]))
			index = index + 1
	for i in range(worker_scale):
		ran = random.randint(0, CLASS_TYPE - 1)
		check = 0
		for j in range(TIME_PERIOD):
			if check == 0 and classType[ran][j] == 1:
				check = 1
				start_employ[i] = j
		empSlot[i] = classType[ran]


	#param dt(Determine the termianl of duty j in period k)
	for j in range(duty_scale):
		ran = random.randint(0, 1)
		terminal_duty[j] = ran + 1

	#param pwt(Terminal of workers)
	for i in range(worker_scale):
		ran = random.randint(0, 1)
		terminal_employ[i] = ran + 1

	#param ds(Duty skill requirement)
	for i in range(duty_scale):
		ran = random.randint(0, skill_scale)
		skill = []
		for j in range(skill_scale):
			if j == ran:
				skill.append(1)
			else:
				skill.append(0)
		skill_duty[i] = skill

	#param ws(Workers' skills)
	for i in range(worker_scale):
		skill = []
		for j in range(skill_scale):
			ran = random.randint(0, 1)
			skill.append(ran)
		skill_emply[i] = skill

	#param pd(Piority of duty)
	for i in range(duty_scale):
		ran = random.randint(1, PIORITY)
		priority[i] = ran

	#Pack to tuple
	for i in range(duty_scale):
		Output["dutyList"].append((i, date, start_duty[i], time[i], demandSlot[i], terminal_duty[i], priority[i], skill_duty[i]))
	for i in range(worker_scale):
		Output["empList"].append((i, date, start_employ[i], empSlot[i], skill_emply[i]))
	Output["priority"] = priority

#generate data with assign factor
def main(worker_num, duty_num, skill_num, demand_num):
	global worker_scale 
	global duty_scale
	global group_scale
	global skill_scale
	global demand_scale
	worker_scale = worker_num
	duty_scale = duty_num
	group_scale = 1
	skill_scale = skill_num
	demand_scale = demand_num
	with open("inputForGreedy.txt", "w") as f:
		param_generator(f)

	return Output

if __name__=="__main__":
	main()