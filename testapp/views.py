from django.shortcuts import render,redirect
from testapp.models import EmployeeModel
from testapp import forms

# Create your views here.

def retrieve_data(request):
    employee=EmployeeModel.objects.all()
    my_dict={'employee':employee}
    return render(request,'html/retrieve.html',my_dict)

def insert_data(request):
    form=forms.EmployeeForm()
    my_dict={'form':form}
    if request.method=='POST':
        form=forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'html/iinsert.html',my_dict)



def delete_data(request,id):
    employee=EmployeeModel.objects.get(id=id)
    employee.delete()
    return redirect('/retrieve')


def update_data(request,id):
    employee=EmployeeModel.objects.get(id=id)
    my_dict={'employee':employee}
    if request.method=='POST':
        form=forms.EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/retrieve')




    return render(request,'html/update.html',my_dict)
