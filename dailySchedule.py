import sys
from random import *
from operator import *
import numpy as np
# from psy2 import *
from datetime import *
import copy as cp
from json import *
# import names
# from jsonFile import *
# from Class import *
# from DayGenerator import *

###################################################################################
#Call data, chart = Greedy(dutylist, emplist) for output 
####################################################################################
PriorColorDict = {1: '#FF0000', 2: '#FF8800', 3: '#FFFF00', 4: '#FF00FF', 5: '#7700FF', 6: '#0000FF'}

class Duty:
	def __init__(self, i, date, start, time, demandSlot, terminal, priority, skill):
		self.id = i
		self.date = date
		self.start = start
		self.time = time
		self.end = start + time 
		self.demandSlot = demandSlot
		self.remainSlot = demandSlot
		self.terminal = terminal
		self.priority = priority
		self.count = 0  #For the count
		self.skill = skill
		# self.skill = dutyDict[self.id].skillList
class EmpSchedule:
	def __init__(self, eid, date, start, empSlot, skill):
		self.eid = eid
		self.date = date
		self.start = start
		# self.seasonSlot = []
		self.empSlot = empSlot
		self.terminalNow = [0 for i in range(len(empSlot))]
		# self.terminal = employeeDict[self.eid].terminal
		self.lastFinish = 0
		self.skill = skill
		# self.skill = employeeDict[self.eid].skill
		self.dutyList = []

TerminalNum = 2
class dayschedule:
	"""docstring for ds"""
	def __init__(self, emplist, dutylist):
		self.emplist = sorted(emplist, key = lambda x: (x.start))
		self.dutylist = sorted(dutylist, key = lambda x: (x.priority*-1, x.time, x.start))
		self.remainEmp = [0 for i in range(len(self.emplist[0].empSlot))]
		for emp in self.emplist:
			self.remainEmp = list(np.add(self.remainEmp, emp.empSlot))
		self.remainTerEmp = [self.remainEmp for j in range(TerminalNum+1)]
		self.assignList = [] # Duty assigned
		self.remainList = [] # Remained after divided	
		self.divideList = [] # Duty fully divided 
		self.sumRemainedDuty = [0 for i in range(len(self.emplist[0].empSlot))]
	def JsonGene(self):
		data = []
		for emp in self.emplist:
			cateSeg = {}
			cateSeg['category'] = str(emp.eid) 
			segList = []
			if len(emp.dutyList) != 0:
				for work in emp.dutyList:
					d = {}
					d['start'] = work.start * 15
					d['starttime'] = str(work.start / 4) + ':' + str(work.start % 4 * 15)
					d['duration'] = work.time * 15
					d['color'] = PriorColorDict[work.priority]
					d['task'] = work.id
					segList.append(d)
				cateSeg['segments'] = segList
				data.append(cateSeg)
		return data
	def chart(self):
		sumEmp = [0 for i in range(len(self.emplist[0].empSlot))]
		sumDuty = [0 for i in range(len(self.emplist[0].empSlot))]
		sumRemained = [0 for i in range(len(self.emplist[0].empSlot))]
		for emp in self.emplist:
			sumEmp = list(np.add(sumEmp, emp.empSlot))
		for duty in self.dutylist:
			sumDuty = list(np.add(sumDuty, duty.demandSlot))
		sumRemained = list(np.subtract(sumEmp, sumDuty))
		chart = []
		chart.append(sumEmp)
		chart.append(sumDuty)
		chart.append(sumRemained)
		return chart
	def needMoving(self, duty, emp):
		if duty.terminal == 0 or emp.terminalNow[duty.start] == 0 or emp.terminalNow[duty.start] == duty.terminal:
			return False
		else:
			return True
	def cutDuty(self, duty, dutyAssigned, assignSlot):
		dutyAssigned.remainSlot = assignSlot
		dutyAssigned.start = dutyAssigned.remainSlot.index(1)
		dutyAssigned.time = dutyAssigned.remainSlot.count(1)
		dutyAssigned.end = len(dutyAssigned.remainSlot) - dutyAssigned.remainSlot[::-1].index(1)
		duty.remainSlot = list(np.subtract(duty.remainSlot, assignSlot))				
		if duty.remainSlot.count(1) > 0:
			duty.start = duty.remainSlot.index(1)
			duty.time = duty.remainSlot.count(1)
			duty.end = len(duty.remainSlot) - duty.remainSlot[::-1].index(1)
		else:
			duty.start = 0
			duty.time = 0 
			duty.end = 0
	def skillSatisfied(self, duty, emp):
		skill = np.subtract(emp.skill, duty.skill)
		return list(skill).count(-1) == 0
	def getRemainEmp(self, duty, emp):
		for terminal in range(len(self.remainTerEmp)):
			if terminal is emp.terminalNow[duty.start] or terminal is 0:
				self.remainTerEmp[terminal] = list(np.subtract(self.remainTerEmp[terminal], duty.remainSlot))
			else:
				self.remainTerEmp[terminal] = list(np.subtract(self.remainTerEmp[terminal], duty.remainSlot))
				if duty.end < len(self.remainTerEmp[terminal]) and emp.empSlot[duty.end] is 1:
					self.remainTerEmp[terminal][duty.end] = max(self.remainTerEmp[terminal][duty.end] - 1, 0)
					if duty.end < len(self.remainTerEmp[terminal])-1 and emp.empSlot[duty.end+1] is 1:
						self.remainTerEmp[terminal][duty.end+1] = max(self.remainTerEmp[terminal][duty.end+1] - 1, 0)		
		# print duty.id, duty.terminal, '\n', emp.empSlot, '\n'
		# for terminal in self.remainTerEmp:
		# 	print terminal, '\n'
	def dutyAssign(self, duty, emp):
		emp.empSlot = [duty.id if duty.remainSlot[i] == 1 and emp.empSlot[i] == 1 else emp.empSlot[i] 
			for i in range(len(emp.empSlot))]
		emp.lastFinish = len(duty.remainSlot) - 1 - duty.remainSlot[::-1].index(1)
		emp.terminalNow = [duty.terminal if duty.start <= time < duty.end else emp.terminalNow[time] 
			for time in range(len(emp.terminalNow))]
		emp.dutyList.append(duty)
		self.getRemainEmp(duty, emp)	
	def getContDuty(self, duty, emp, afford):
		start = afford.index(1)
		end = len(afford) - afford[::-1].index(1)
		maxTime = 0
		maxStart = start
		maxEnd = start
		count = 0
		for time in range(start, end):
			if afford[time] == 1:
				count += 1
				maxEnd = time + 1
			else:
				count = 0
				maxStart = time + 1
			if count > maxTime:
				Tstart = maxStart
				Tend = maxEnd
				maxTime = count
		affordSlot = [1 if Tstart <= time < Tend else 0 for time in range(len(emp.empSlot))]
		return affordSlot
	def checkDutyAfford(self, duty, emp):
		afford = [1 if emp.empSlot[time] == 1 and duty.remainSlot[time] == 1 else 0 for time in range(len(emp.empSlot))]
		if not self.skillSatisfied(duty, emp):
			affordSlot = [0 for i in range(len(emp.empSlot))]
		elif afford.count(1) == 0:
			affordSlot = [0 for i in range(len(emp.empSlot))]
		else:
			afford = self.getContDuty(duty, emp, afford)
			start = afford.index(1)
			end = len(afford) - afford[::-1].index(1)
			Tstart = start + 2
			moveStart = emp.terminalNow[max(start-1, 0)]
			if moveStart == duty.terminal or moveStart == 0:
				Tstart = start + 1
				moveStart = emp.terminalNow[max(start-2, 0)]
				if moveStart == duty.terminal or moveStart == 0:
					Tstart = start
			Tend = end - 2
			moveEnd = emp.terminalNow[min(end, len(emp.terminalNow)-1)]
			if  moveEnd == duty.terminal or moveEnd == 0:
				Tend = end - 1
				moveEnd = emp.terminalNow[min(end+1, len(emp.terminalNow)-1)]
				if moveEnd == duty.terminal or moveEnd == 0:
					Tend = end
			affordSlot = [afford[time] if Tstart <= time < Tend else 0 for time in range(len(emp.empSlot))]
		return affordSlot	
	def dutydivide(self, duty, emplist):
		# dutyRemain = duty.remainSlot
		while sum(duty.remainSlot) > 0:
			maxTime = 0
			empid = 0
			maxSlot = []
			for i in range(len(self.emplist)):
				emp = self.emplist[i]
				afford = self.checkDutyAfford(duty, emp)
				affordTime = sum(afford)
				if  affordTime > maxTime:
					maxTime = affordTime
					maxSlot = afford
					empid = i
			if maxTime == 0:
				self.remainList.append(duty)
				break
			dutyAssigned = cp.deepcopy(duty) #dont shallow copy fck u
			self.cutDuty(duty, dutyAssigned, maxSlot)
			self.dutyAssign(dutyAssigned, self.emplist[empid])	
	
	def greedy(self):
		chart = self.chart()
		self.lastAssignList = []
		for duty in self.dutylist:
			start = duty.start
			end = duty.start + duty.time
			terminal = duty.terminal
			empMoving = []
			for empNum in range(len(self.emplist)):
				emp = self.emplist[empNum]
				if self.skillSatisfied(duty, emp):
					afford = self.checkDutyAfford(duty,emp)
					if afford.count(1) == duty.time:
						if not self.needMoving(duty,emp):
							self.assignList.append(duty)
							self.dutyAssign(duty, emp)
							break
						else:
							if emp.empSlot[start-1] == 1 and emp.empSlot[start-2] == 1:
								empMoving.append(empNum)
				if 	empNum is len(self.emplist)-1:				
					#Employee need move between terminal
					if len(empMoving) != 0:
						Min = 1000
						MinEmp = 0
						for num in empMoving:
							FromLastDuty = duty.start - self.emplist[num].lastFinish
							if FromLastDuty < Min:
								Min = FromLastDuty
								MinEmp = num
						self.assignList.append(duty)
						self.dutyAssign(duty, self.emplist[MinEmp])
					# Duty Can be divided to complete
					else:
						totalForce= [0 for i in range(len(emp.empSlot))]
						for emp in self.emplist:
							if self.skillSatisfied(duty, emp):
								afford = self.checkDutyAfford(duty,emp)
								totalForce = list(np.add(totalForce, afford))
						if list(np.subtract(totalForce, duty.remainSlot)).count(-1) == 0:						
							dutyCopy = cp.deepcopy(duty)
							self.divideList.append(dutyCopy) 
							self.dutydivide(duty, self.emplist)
						else:
							self.lastAssignList.append(duty)
		#Remain duty can not be divided completely
		for duty in self.lastAssignList:
			self.dutydivide(duty, self.emplist)
		data = self.JsonGene()
		# print data, chart
		return data, chart
	# print js 
def Greedy(dutylist, emplist):
		# if __name__ == "__main__":
	for d in range(len(dutylist)):
		duty = dutylist[d]
		dutylist[d] = Duty(duty[0], duty[1], duty[2], duty[3], duty[4], duty[5], duty[6], duty[7])
	for e in range(len(emplist)):
		emp = emplist[e]
		emplist[e] = EmpSchedule(emp[0], emp[1], emp[2], emp[3], emp[4])
	ds = dayschedule(emplist, dutylist)
	data, chart = ds.greedy()
	for duty in ds.remainList:
		ds.sumRemainedDuty = np.add(ds.sumRemainedDuty, duty.remainSlot)

	pr = 1
	if pr == 1:
		print "_____________emptime__________________"
		for i in range(len(ds.emplist)):
			print i, " ", ds.emplist[i].empSlot
		# print "________remain employee_________________"
		# print ds.remainTerEmp[0] ,'\n', ds.remainTerEmp[1] ,'\n', ds.remainTerEmp[2] 
		# print "________sum of remain duty_____________"
		# print ds.sumRemainedDuty
	print "_______", len(ds.assignList), " assign duty___________"
	for duty in ds.assignList:
			print duty.id,
			# print duty.id, duty.terminal, duty.remainSlot
	print "__________________", len(ds.divideList), "divide duty_________________________"
	for duty in ds.divideList:
			print duty.id,
			# print duty.id, duty.terminal, duty.demandSlot
	print "___________", len(ds.remainList)," remain duty____________________"
	for duty in ds.remainList:
			print duty.id,
			# print duty.id , duty.terminal, duty.remainSlot
	# 	print "___________duty_______________________"
	# 	for duty in ds.dutylist:
	# 		print duty.id, duty.terminal, duty.demandSlot
	return data, chart
# output1, output2 = Greedy(dutylist, emplist)
