from django.shortcuts import render, redirect
from employeeform.models import Employee
from form.models import StudentInfo
from .models import StudentLeave, EmployeeLeave
from datetime import date
from accounts.models import UserProfile
from classform.models import ClassRoom, ClassRoomStudent
# Create your views here.


def employee_leave(request):
    """
    Employees request for leave
    Input: Subject, Date From and To, Leave Description
    """
    if request.method == "POST":
        emp_id = request.POST.get("emp_id")
        description = request.POST.get("description")
        subject = request.POST.get("subject")
        date_to = request.POST.get("date_to")
        date_from = request.POST.get("date_from")
        date_to = date(*map(int, date_to.split('-')))
        date_from = date(*map(int, date_from.split('-')))
        EmployeeLeave.objects.create(employee=Employee.objects.get(
            empID=emp_id), description=description, subject=subject, date_from=date_from, date_to=date_to)
    return render(request, "leave/employee.html")


def student_leave(request):
    """
    Student request for leave
    Input: Subject, Date From and To, Leave Description
    """
    if request.method == "POST":
        admissionNumber = request.POST.get("admissionNumber")
        description = request.POST.get("description")
        subject = request.POST.get("subject")
        date_to = request.POST.get("date_to")
        date_from = request.POST.get("date_from")
        date_to = date(*map(int, date_to.split('-')))
        date_from = date(*map(int, date_from.split('-')))
        StudentLeave.objects.create(student=StudentInfo.objects.get(
            admissionNumber=admissionNumber), description=description, subject=subject, date_from=date_from, date_to=date_to)
    return render(request, "leave/student.html")


def view_student_leaves(request):
    """
    Display the leaves request to the teacher
    """
    leaves = StudentLeave.objects.filter(approved=False, rejected=False)
    if len(leaves) == 0:
        return render(request, "leave/studentLeaveRequest.html")
    else:
        return render(request, "leave/studentLeaveRequest.html", {"leaves": leaves})

def view_teacher_leaves(request):
    """
    Display the leaves request to the teacher
    """
    leaves = EmployeeLeave.objects.filter(approved=False, rejected=False)
    if len(leaves) == 0:
        return render(request, "leave/teacherLeaveRequest.html")
    else:
        return render(request, "leave/teacherLeaveRequest.html", {"leaves": leaves})

def approve_leave(request, id):
    """
    Aprrove the leave requests of the students
    """
    leave = StudentLeave.objects.get(id=id)
    leave.approved = True
    leave.save()
    leaves = StudentLeave.objects.filter(approved=False, rejected=False)
    if len(leaves) == 0:
        return render(request, "leave/studentLeaveRequest.html")
    else:
        return render(request, "leave/studentLeaveRequest.html", {"leaves": leaves})

def reject_leave(request, id):
    """
    Rejcect the leave request of the student
    """
    leave = StudentLeave.objects.get(id=id)
    leave.rejected = True
    leave.save()
    leaves = StudentLeave.objects.filter(approved=False, rejected=False)
    if len(leaves) == 0:
        return render(request, "leave/studentLeaveRequest.html")
    else:
        return render(request, "leave/studentLeaveRequest.html", {"leaves": leaves})

def approve_leavet(request, id):
    """
    Aprrove the leave requests of the students
    """
    leave = EmployeeLeave.objects.get(id=id)
    leave.approved = True
    leave.save()
    leaves = EmployeeLeave.objects.filter(approved=False, rejected=False)
    if len(leaves) == 0:
        return render(request, "leave/teacherLeaveRequest.html")
    else:
        return render(request, "leave/teacherLeaveRequest.html", {"leaves": leaves})

def reject_leavet(request, id):
    """
    Rejcect the leave request of the student
    """
    leave = EmployeeLeave.objects.get(id=id)
    leave.rejected = True
    leave.save()
    leaves = EmployeeLeave.objects.filter(approved=False, rejected=False)
    if len(leaves) == 0:
        return render(request, "leave/teahcerLeaveRequest.html")
    else:
        return render(request, "leave/teacherLeaveRequest.html", {"leaves": leaves})
def showstudentleave(request):
    user_profile =UserProfile.objects.get(user=request.user)
    addmission_number = user_profile.addmission_number
    leaves = StudentLeave.objects.filter(student__admissionNumber=addmission_number)
    return render(request, "leave/showstudentleave.html",{'leaves': leaves})
def showteacherleave(request):
    user_profile =UserProfile.objects.get(user=request.user)
    emp_id = user_profile.emp_id
    leaves = EmployeeLeave.objects.filter(employee__empID=emp_id)
    return render(request, "leave/showteacherleave.html",{'leaves': leaves})