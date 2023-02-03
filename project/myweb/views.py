from django.shortcuts import render,redirect,get_object_or_404
from .models import StudentInfo
from .forms import CreateStudent
from django.contrib import messages
# Create your views here.



def home(request):
    return render(request,template_name="home.html")

def logout(request):
    return render(request,template_name="accounts/login.html")

def student_registration(request):
    if request.method == "POST":
        forms = CreateStudent(request.POST)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Student Registration Successfully!")
        return redirect("myweb:student_list")
    else:
        forms = CreateStudent()

    return render(request,"students/registration.html", context={"forms":forms})


def edit_student(request, pk):
    student_edit = StudentInfo.objects.get(id=pk)
    edit_forms = CreateStudent(instance=student_edit)

    if request.method == "POST":
        edit_forms = CreateStudent(request.POST, instance=student_edit)

        if edit_forms.is_valid():
            edit_forms.save()
            messages.success(request, "Edit Student Info Successfully!")
            return redirect("myweb:student_list")

    return render(request, "students/edit_student.html", context={"edit_forms":edit_forms})

def delete_student(request, student_id):
    student_delete = StudentInfo.objects.get(id=student_id)
    student_delete.delete()
    messages.success(request, "Delete Student Info Successfully")
    return redirect("myweb:student_list")



def student_list(request):
    students = StudentInfo.objects.all()
    return render(request, "students/student_list.html", context={"students":students})


def single_student(request, student_id):
    single_student = get_object_or_404(StudentInfo, pk=student_id)
    return render(request,"students/student_details.html", context={"single_student":single_student})