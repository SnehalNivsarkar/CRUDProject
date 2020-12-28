from django.shortcuts import render,redirect
from crudapp.models import Student
from crudapp import forms
# Create your views here.
def read_data(request):
    student_details = Student.objects.order_by('sno')
    my_dict = {'student_details':student_details}
    return render(request,'html/read.html',my_dict)

def insert_data(request):
    form = forms.StudentForm()
    my_dict = {'form':form}

    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/read')
    return render(request,'html/insert.html',my_dict)

def delete_data(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/read')

def update_data(request,id):
    student=Student.objects.get(id=id)
    my_dict={'student':student}
    if request.method=='POST':
        form=forms.StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/read')

    return render(request,'html/update.html',my_dict)


def back(request):
    return render(request,'html/read.html')
