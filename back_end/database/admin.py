from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources


from .models import Airline
from .models import AirlineAgreement
from .models import Model
from .models import CheckInRatioF
from .models import CheckInRatioC
from .models import CheckInRatioY
from .models import CheckInRatioG
from .models import Flight
from .models import Group
from .models import Employee
from .models import Skill
from .models import EmployeeSkill
from .models import Duty
from .models import DutySkill
from .models import BlackListAirline
from .models import BlackListEmployee
from .models import SeasonalSchedule
from .models import AssignedDuty
from .models import PersonalSchedule


class AirlineResource(resources.ModelResource):
    class Meta:
        model = Airline
        exclude = ('createdAt', 'updatedAt')
        import_id_fields = ['code']

class AirlineAdmin(ImportExportModelAdmin):
    resource_class = AirlineResource
    pass

class AirlineAgreementResource(resources.ModelResource):
    class Meta:
        model = AirlineAgreement
        exclude = ('createdAt', 'updatedAt')
        import_id_fields = ['name']

class AirlineAgreementAdmin(ImportExportModelAdmin):
    resource_class = AirlineAgreementResource
    pass

class GroupResource(resources.ModelResource):
    class Meta:
        model = Group
        exclude = ('createdAt', 'updatedAt')
        import_id_fields = ['code']

class GroupAdmin(ImportExportModelAdmin):
    resource_class = GroupResource
    pass

class FlightResource(resources.ModelResource):
    class Meta:
        model = Flight
        exclude = ('createdAt', 'updatedAt')

class FlightAdmin(ImportExportModelAdmin):
    resource_class = FlightResource
    pass

class CheckInRatioFResource(resources.ModelResource):
    class Meta:
        model = CheckInRatioF
        exclude = ('createdAt', 'updatedAt')

class CheckInRatioFAdmin(ImportExportModelAdmin):
    resource_class = CheckInRatioFResource
    pass

class CheckInRatioCResource(resources.ModelResource):
    class Meta:
        model = CheckInRatioC
        exclude = ('createdAt', 'updatedAt')

class CheckInRatioCAdmin(ImportExportModelAdmin):
    resource_class = CheckInRatioCResource
    pass

class CheckInRatioYResource(resources.ModelResource):
    class Meta:
        model = CheckInRatioY
        exclude = ('createdAt', 'updatedAt')

class CheckInRatioYAdmin(ImportExportModelAdmin):
    resource_class = CheckInRatioYResource
    pass

class CheckInRatioGResource(resources.ModelResource):
    class Meta:
        model = CheckInRatioG
        exclude = ('createdAt', 'updatedAt')

class CheckInRatioGAdmin(ImportExportModelAdmin):
    resource_class = CheckInRatioGResource
    pass

admin.site.register(Airline, AirlineAdmin)
admin.site.register(AirlineAgreement, AirlineAgreementAdmin)
admin.site.register(Model)
admin.site.register(CheckInRatioF, CheckInRatioFAdmin)
admin.site.register(CheckInRatioC, CheckInRatioCAdmin)
admin.site.register(CheckInRatioY, CheckInRatioYAdmin)
admin.site.register(CheckInRatioG, CheckInRatioGAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Employee)
admin.site.register(Skill)
admin.site.register(EmployeeSkill)
admin.site.register(Duty)
admin.site.register(DutySkill)
admin.site.register(BlackListAirline)
admin.site.register(BlackListEmployee)
admin.site.register(SeasonalSchedule)
admin.site.register(AssignedDuty)
admin.site.register(PersonalSchedule)
