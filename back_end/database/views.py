from math import ceil
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from database.models import Flight
from database.models import Group
from database.models import Duty

def index(request):
	# clear the original Duty table and insert new duties based on flights
	flights = Flight.objects.all()
	duties = Duty.objects.all()
	jobID = 1
	if duties:
		duties.delete()
	for flight in flights:
		if flight.flightType == 'DEP':
			numCTR = dict.fromkeys(['240', '210', '180', '150', '120', '90', '60', '30'],0)
			for i in ['F','C','Y','G']:
				if i == 'G':			
					numPassenger = flight.numPassengerY * flight.groupRatio
				elif i == 'Y':
					numPassenger = flight.numPassengerY * (1 - flight.groupRatio)
				else:	
					numPassenger = 'numPassenger'+ i
					numPassenger = getattr(flight, numPassenger)
				field = 'checkInRatio'+ i
				checkInRatio = getattr(flight, field)
				field = 'serviceLevel'+ i
				serviceLevel = getattr(flight, field)
				
				numCTR['240'] += ceil(numPassenger * checkInRatio.min240 * serviceLevel)
				numCTR['210'] += ceil(numPassenger * checkInRatio.min210 * serviceLevel)
				numCTR['180'] += ceil(numPassenger * checkInRatio.min180 * serviceLevel)
				numCTR['150'] += ceil(numPassenger * checkInRatio.min150 * serviceLevel)
				numCTR['120'] += ceil(numPassenger * checkInRatio.min120 * serviceLevel)
				numCTR['90'] += ceil(numPassenger * checkInRatio.min90 * serviceLevel)
				numCTR['60'] += ceil(numPassenger * checkInRatio.min60 * serviceLevel)
				numCTR['30'] += ceil(numPassenger * checkInRatio.min30 * serviceLevel)		
				
			# insert CTR duties
			departureTime = flight.departureTime	
			for i in range(1,9):
				HRDemand = numCTR[str(30*i)]
				dutyStartTime = departureTime - datetime.timedelta(minutes = 30*i)
				dutyEndTime = departureTime - datetime.timedelta(minutes = 30*(i-1))
				if HRDemand > 0:
					newDuty = Duty(name = str(flight.flightNum)+' CTR', group = Group.objects.get(code='CTR'), flightID= flight, jobID = jobID, HRDemand = HRDemand, startTime = dutyStartTime, endTime = dutyEndTime, femaleDemand = 0, maleDemand = 0)
					newDuty.save() # all CTR duties have same jobID
					jobID += 1
		# insert CIQ duties
		if flight.flightType == 'ARR':	
			dutyStartTime = flight.arrivalTime - datetime.timedelta(minutes = 15)
			dutyEndTime = flight.arrivalTime + datetime.timedelta(minutes = 20)
			newDuty = Duty(name = str(flight.flightNum)+' LI', group = Group.objects.get(code='CIQ'), flightID= flight, jobID = jobID, HRDemand = 1, startTime = dutyStartTime, endTime = dutyEndTime, femaleDemand = 0, maleDemand = 0)
			newDuty.save()
			jobID += 1
			
			dutyStartTime = flight.arrivalTime - datetime.timedelta(minutes = 5)
			dutyEndTime = flight.arrivalTime + datetime.timedelta(minutes = 20)
			newDuty = Duty(name = str(flight.flightNum)+' B4', group = Group.objects.get(code='CIQ'), flightID= flight, jobID = jobID, HRDemand = 1, startTime = dutyStartTime, endTime = dutyEndTime, femaleDemand = 0, maleDemand = 0)
			newDuty.save()
			jobID += 1
		else:
			if flight.model != '747' and flight.model != '777':
				num = range(1,3)
			else:
				num = range(1,4)

			departureTime = flight.departureTime
			for i in num:
				dutyStartTime = departureTime - datetime.timedelta(minutes = 70)
				dutyEndTime = departureTime
				name = ' BG' + str(i)
				newDuty = Duty(name = str(flight.flightNum)+name, group = Group.objects.get(code='CIQ'), flightID= flight, jobID = jobID, HRDemand = 1, startTime = dutyStartTime, endTime = dutyEndTime, femaleDemand = 0, maleDemand = 0)
				newDuty.save()
				jobID += 1

			dutyStartTime = departureTime - datetime.timedelta(minutes = 60)
			dutyEndTime = departureTime + datetime.timedelta(minutes = 10)
			newDuty = Duty(name = str(flight.flightNum)+' LO1', group = Group.objects.get(code='CIQ'), flightID= flight, jobID = jobID, HRDemand = 1, startTime = dutyStartTime, endTime = dutyEndTime, femaleDemand = 0, maleDemand = 0)
			newDuty.save()
			jobID += 1

			if flight.flightRoute == 'SYO' or flight.destination == 'EUR' or flight.destination == 'USA':
				dutyStartTime = departureTime - datetime.timedelta(minutes = 90)
				dutyEndTime = departureTime
				newDuty = Duty(name = str(flight.flightNum)+' SECURITY', group = Group.objects.get(code='CIQ'), flightID= flight, jobID = jobID, HRDemand = 1, startTime = dutyStartTime, endTime = dutyEndTime, femaleDemand = 0, maleDemand = 0)
				newDuty.save()
				jobID += 1
	

	# http response	
	return HttpResponse('TABLE "Duty" reset')
