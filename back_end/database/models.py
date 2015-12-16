from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

class Airline(models.Model):
	code = models.CharField(max_length=30, primary_key=True)
	name = models.CharField(max_length=30)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name

class AirlineAgreement(models.Model):
	name = models.CharField(max_length=30, primary_key=True)
	minNumCTR = models.IntegerField(default=0)
	minNumCIQ = models.IntegerField(default=0)
	startCtrTime = models.IntegerField(default=120)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name

class Model(models.Model):
	name = models.CharField(max_length=30)
	numF = models.IntegerField(default=0)
	numC = models.IntegerField(default=0)
	numY = models.IntegerField(default=0)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name

class CheckInRatioF(models.Model):
	name = models.CharField(primary_key=True,max_length=30)
	min240 = models.FloatField(default=0.0)
	min210 = models.FloatField(default=0.0)
	min180 = models.FloatField(default=0.0)
	min150 = models.FloatField(default=0.0)
	min120 = models.FloatField(default=0.0)
	min90 = models.FloatField(default=0.0)
	min60 = models.FloatField(default=0.0)
	min30 = models.FloatField(default=0.0)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name

class CheckInRatioC(models.Model):
	name = models.CharField(primary_key=True,max_length=30)
	min240 = models.FloatField(default=0.0)
	min210 = models.FloatField(default=0.0)
	min180 = models.FloatField(default=0.0)
	min150 = models.FloatField(default=0.0)
	min120 = models.FloatField(default=0.0)
	min90 = models.FloatField(default=0.0)
	min60 = models.FloatField(default=0.0)
	min30 = models.FloatField(default=0.0)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name

class CheckInRatioY(models.Model):
	name = models.CharField(primary_key=True,max_length=30)
	min240 = models.FloatField(default=0.0)
	min210 = models.FloatField(default=0.0)
	min180 = models.FloatField(default=0.0)
	min150 = models.FloatField(default=0.0)
	min120 = models.FloatField(default=0.0)
	min90 = models.FloatField(default=0.0)
	min60 = models.FloatField(default=0.0)
	min30 = models.FloatField(default=0.0)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name

class CheckInRatioG(models.Model):
	name = models.CharField(primary_key=True,max_length=30)
	min240 = models.FloatField(default=0.0)
	min210 = models.FloatField(default=0.0)
	min180 = models.FloatField(default=0.0)
	min150 = models.FloatField(default=0.0)
	min120 = models.FloatField(default=0.0)
	min90 = models.FloatField(default=0.0)
	min60 = models.FloatField(default=0.0)
	min30 = models.FloatField(default=0.0)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name


class Flight(models.Model):
	flightNum = models.CharField(max_length=30)
	airline = models.ForeignKey(Airline,to_field='code')
	model = models.CharField(max_length=30)
	modelNumF = models.IntegerField(default=0)
	modelNumC = models.IntegerField(default=0)
	modelNumY = models.IntegerField(default=0)
	terminal = models.CharField(max_length=30)
	counter = models.IntegerField(null=True, blank=True)
	flightRoute = models.CharField(max_length=30)
	gate = models.CharField(max_length=30)
	origin = models.CharField(max_length=30)
	destination = models.CharField(max_length=30)
	flightType = models.CharField(max_length=30)
	departureTime = models.DateTimeField(null=True, blank=True)
	arrivalTime = models.DateTimeField(null=True, blank=True)
	numPassengerF = models.IntegerField(null=True, blank=True)
	numPassengerC = models.IntegerField(null=True, blank=True)
	numPassengerY = models.IntegerField(null=True, blank=True)
	checkInRatioF = models.ForeignKey(CheckInRatioF,default='general', null=True, blank=True)
	checkInRatioC = models.ForeignKey(CheckInRatioC,default='general', null=True, blank=True)
	checkInRatioY = models.ForeignKey(CheckInRatioY,default='general', null=True, blank=True)
	checkInRatioG = models.ForeignKey(CheckInRatioG,default='general', null=True, blank=True)
	serviceLevelF = models.FloatField(default=0.0, null=True, blank=True)
	serviceLevelC = models.FloatField(default=0.0, null=True, blank=True)
	serviceLevelY = models.FloatField(default=0.0, null=True, blank=True)
	serviceLevelG = models.FloatField(default=0.0, null=True, blank=True)
	groupRatio = models.FloatField(default=0.0, null=True, blank=True)
	airlineAgreement = models.ForeignKey(AirlineAgreement)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)

	def setStartCTRTime(self):
		return self.departureTime - datetime.timedelta(minutes = self.airlineAgreement.startCtrTime)
	startCtrTime = property(setStartCTRTime)

	def setEndCTRTime(self):
		return self.departureTime - datetime.timedelta(minutes = 30)
	endCtrTime = property(setEndCTRTime)

	def clean(self):
		if self.flightType != 'ARR' and self.flightType != 'DEP':
			raise ValidationError('flightType could only have value ARR/DEP')

	def __unicode__(self):
		return self.flightNum

class Group(models.Model):
	code = models.CharField(primary_key=True, max_length=30)
	name = models.CharField(max_length=30)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.code

class Employee(models.Model):
	ID = models.CharField(max_length=30, primary_key=True)
	name = models.CharField(max_length=30)
	gender = models.CharField(max_length=30, default='N/A')
	assignedAirline = models.ForeignKey(Airline)
	group = models.ForeignKey(Group)
	terminal = models.CharField(max_length=30)
	jobLevel = models.CharField(max_length=30)
	salaryLevel = models.CharField(max_length=30)
	contractType = models.CharField(max_length=30)
	isFixed = models.BooleanField()
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.ID

class Skill(models.Model):
	class Meta:
		unique_together = (('name', 'level', 'priority'),)
	name = models.CharField(max_length=30)
	level = models.IntegerField(default=0)
	priority = models.IntegerField(default=0)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name+str(self.level)

class EmployeeSkill(models.Model):
	class Meta:
		unique_together = (('employeeID', 'skillID'),)
	employeeID = models.ForeignKey(Employee)
	skillID = models.ForeignKey(Skill)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name+str(self.level)

class Duty(models.Model):
	name = models.CharField(max_length=30)
	group = models.ForeignKey(Group)
	flightID = models.ForeignKey(Flight)
	jobID = models.IntegerField(default=0)
	HRDemand = models.IntegerField(default=0)
	startTime = models.DateTimeField()
	endTime = models.DateTimeField()
	femaleDemand = models.IntegerField(default=0)
	maleDemand = models.IntegerField(default=0)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.name

class DutySkill(models.Model):
	class Meta:
		unique_together = (('dutyID', 'skillID'),)
	dutyID = models.ForeignKey(Duty)
	skillID = models.ForeignKey(Skill)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.dutyID+self.skillID

class BlackListAirline(models.Model):
	class Meta:
		unique_together = (('employeeID', 'airline'),)
	employeeID = models.ForeignKey(Employee)
	airline = models.ForeignKey(Airline)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.employeeID+self.arline

class BlackListEmployee(models.Model):
	class Meta:
		unique_together = (('employeeID1', 'employeeID2'),)
	employeeID1 = models.ForeignKey(Employee)
	employeeID2 = models.ForeignKey(Employee,  related_name="blackListEmployee2")
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.employeeID1+self.employeeID2

class SeasonalSchedule(models.Model):
	period = models.CharField(max_length=30)
	group = models.ForeignKey(Group)
	assignedAirline = models.ForeignKey(Airline)
	isAgent = models.BooleanField()
	startTime = ArrayField(
		models.DateTimeField(),
		size = 100,
	)
	classType = ArrayField(
		models.CharField(max_length=15),
		size = 100,
	)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.classType + self.startTime + self.classType

class AssignedDuty(models.Model):
	dutyID = models.ForeignKey(Duty)
	employeeID = models.ForeignKey(Employee)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.dutyID + self.employeeID
class PersonalSchedule(models.Model):
	employeeID = models.OneToOneField(Employee, primary_key=True)
	schedule = models.ForeignKey(SeasonalSchedule)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	def __unicode__(self):
		return self.employeeID
class test():
    pass
