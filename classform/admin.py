"""
Admin panel for classroom app
"""
from django.contrib import admin
from .models import ClassRoom, ClassRoomStudent, StudentRouteAttendence ,ClassTable,ReportCard
# Register your models here.
admin.site.register(ReportCard)
admin.site.register(ClassRoom)
admin.site.register(ClassTable)
admin.site.register(ClassRoomStudent)
admin.site.register(StudentRouteAttendence)
