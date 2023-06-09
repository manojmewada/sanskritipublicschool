import tempfile
from tempfile import NamedTemporaryFile
from django.core.files import File
from openpyxl import load_workbook
from datetime import date
from django.shortcuts import render, redirect
from .models import Fine, Fee, FeeCategory, FeeCycle, FeeDiscount, ClassSectionFees
from classform.models import ClassRoomStudent, ClassRoom
import xlwt
import openpyxl
from openpyxl import Workbook
from accounts.models import UserProfile
# Create your views here.


def add_fine(request):
    """
    Add Fine for a student
    Input: Admission Number of the student
    """
    if request.method == "GET":
        category = request.GET.get("category")
        fine = request.GET.get("fine")
        add_number = request.GET.get("add_number")
        description = request.GET.get("description")
        if add_number:
            student = ClassRoomStudent.objects.get(
                student__admissionNumber=add_number)
            Fine.objects.create(fine=fine, category=category,
                                description=description, student=student)
            redirect('addFine')
    return render(request, 'fees/addFine.html')


def set_fee_category(request):
    """
    Set fee category 
    """
    if request.method == "GET":
        description = request.GET.get("description")
        checklist = request.GET.get("check")
        mode = request.GET.get("mode")

        if "recurring" in checklist:
            FeeCategory.objects.create(
                once=False, submission_type=mode, description=description)
        else:
            FeeCategory.objects.create(
                once=True, submission_type="once", description=description)

        return render(request, 'fees/home.html', {"class_rooms": ClassRoom.objects.all()})


def add_fee_class(request):
    """
    Set fee amount for a particular class
    Input: Fee amount, Class-Section and Category
    """
    if request.method == 'GET':
        fees = request.GET.get("fees")
        classSection = request.GET.get("class_room")
        category = request.GET.get("category")
        if category:
            fee_category = FeeCategory.objects.get(submission_type=category)
            classRoom = ClassRoom.objects.get(classSection=classSection)
            ClassSectionFees.objects.create(classSection=classRoom,
                                            feeCategory=fee_category, fees=fees)
            redirect('addFeeClass')
    return render(request, 'fees/addClassFee.html', {"category": FeeCategory.objects.all(), "class_rooms": ClassRoom.objects.all()})


def add_fee_cycle(request):
    """
    Set fee cycle for the Fee Payement
    Input: Cycle Type, Starting and Ending Date
    """
    if request.method == 'GET':
        cycle = request.GET.get("cycle")
        starting_date = request.GET.get("starting_date")
        ending_date = request.GET.get("ending_date")
        starting_date = date(*map(int, starting_date.split('-')))
        ending_date = date(*map(int, ending_date.split('-')))
        FeeCycle.objects.create(
            lastSubmissionDate=ending_date, firstSubmissionDate=starting_date, cycle=cycle)

    return render(request, 'fees/home.html')


def home(request):
    if request.method == 'POST':
        classSection = request.POST.get("class_room")
        payment_method = request.POST.get("payment_method")
        amount = request.POST.get("amount")
        reg_no = request.POST.get("register_number")
        months = request.POST.get("months")
        add_number = request.POST.get("add_number")
        if "excel" in request.FILES:
            fee_slip_excell = request.FILES["excel"]
        if add_number and fee_slip_excell:
            classRoom = ClassRoom.objects.get(classSection=classSection)
            student = ClassRoomStudent.objects.get(
                student__admissionNumber=add_number)
            wb = load_workbook(fee_slip_excell)
            
            sheet = wb.get_sheet_by_name('Sheet2')
            # set slip no, name, class, date, months, class, amount

            # 1st copy
            sheet["B9"] = reg_no
            sheet["B10"] = add_number
            sheet["B12"] = student.student.admissionNumber
            sheet["G10"] = date.today().strftime("%B %d, %Y")
            sheet["G11"] = months
            sheet["E15"] = amount
            sheet["C20"] = amount

            # 2nd copy
            sheet["I9"] = reg_no
            sheet["I10"] = add_number
            sheet["I12"] = student.student.admissionNumber
            sheet["N10"] = date.today().strftime("%B %d, %Y")
            sheet["N11"] = months
            sheet["L15"] = amount
            sheet["J20"] = amount
            
             # 2nd copy
            sheet["K9"] = reg_no
            sheet["K10"] = add_number
            sheet["L12"] = student.student.admissionNumber
            sheet["M10"] = date.today().strftime("%B %d, %Y")
            sheet["N11"] = months
            sheet["O15"] = amount
            sheet["P20"] = amount
             # 2nd copy
            sheet["P9"] = reg_no
            sheet["P10"] = add_number
            sheet["Q12"] = student.student.admissionNumber
            sheet["R10"] = date.today().strftime("%B %d, %Y")
            sheet["S11"] = months
            sheet["T15"] = amount
            sheet["V20"] = amount

            #wb.save('fee-slip.xlsx')
            #tmp = tempfile.NamedTemporaryFile(delete=False)
            #tmpName =tmp.name
            #wb.save(tmpName)
            #tmp.seek(0)
            with NamedTemporaryFile(delete=False) as tmp:
                wb.save(tmp.name)
                tmp.seek(0)

                Fee.objects.create(regNo=reg_no, student=student, classSection=classRoom, submissionDate=date.today(
                ), monthsPaid=months, payment_method=payment_method, amount=amount)
                fee = Fee.objects.get(student=student, regNo=reg_no, submissionDate=date.today())
                fee.feeSlip.save("fee-slip",File(tmp), True)
                fee.save()

                
                from win32com import client
                from win32com.client import Dispatch
                import win32api
                import pythoncom

                excel = client.Dispatch("Excel.Application",pythoncom.CoInitialize())
                excel.Visible = 0

                wb = excel.Workbooks.Open(tmp.name)
              
                ws = wb.Worksheets[1]
                wb.SaveAs('c:\\manojfeefolder\\feeslip.pdf', FileFormat=57)
                print ("Failed to convert")
                wb.Close()
                excel.Quit()
    return render(request, 'fees/home.html', {"class_rooms": ClassRoom.objects.all()})



def fee_discount(request):
    """
    Add fee discount for a paritcular student
    Input: Admission Number, Discount%, Total Off
    """
    if request.method == "GET":
        description = request.GET.get('description')
        add_number = request.GET.get('add_number')
        total_off = request.GET.get('total_off')
        discount = request.GET.get('discount')
        if discount:
            student = ClassRoomStudent.objects.get(
                student__admissionNumber=add_number)
            FeeDiscount.objects.create(
                discount=discount, student=student, description=description, total_off=total_off)
        return render(request, 'fees/home.html')
    

def showfee(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.user_type == "Student":
        addmission_number = user_profile.addmission_number
        Fees = Fee.objects.filter(student__student__admissionNumber=addmission_number)
        #notice = StudentNotice.objects.filter(student__student= student)
        #notice = StudentNotice.objects.all()
        #if len(Fee)>0:
        return render(request, 'fees/checkFee.html', {"Fee":Fees})
        
        #else:
           # return render(request, 'notice/checkSFee.html')
def showfine(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.user_type == "Student":
        addmission_number = user_profile.addmission_number
        Fines = Fine.objects.filter(student__student__admissionNumber=addmission_number)
        #notice = StudentNotice.objects.filter(student__student= student)
        #notice = StudentNotice.objects.all()
        #if len(Fee)>0:
        return render(request, 'fees/checkFine.html', {"Fine":Fines})
    