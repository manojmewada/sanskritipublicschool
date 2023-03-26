from django.urls import path
from . import views

urlpatterns = [
    path('employeeLeave/', views.employee_leave, name="employeeLeave"),
    path('studentLeave/', views.student_leave, name="studentLeave"),
    path('viewStudentLeaves/', views.view_student_leaves, name="viewStudentLeaves"),
    path('viewTeacherLeaves/', views.view_teacher_leaves, name="viewTeacherLeaves"),
    path('approveLeave/<int:id>/', views.approve_leave, name="approveLeave"),
    path('rejectLeave/<int:id>/', views.reject_leave, name="rejectLeave"),
    path('approveLeavet/<int:id>/', views.approve_leavet, name="approveLeavet"),
    path('rejectLeavet/<int:id>/', views.reject_leavet, name="rejectLeavet"),
    path('showstudentLeave/', views.showstudentleave, name="showstudentLeave"),
    path('showteacherLeave/', views.showteacherleave, name="showteacherLeave"),
]