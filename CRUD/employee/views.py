from django.shortcuts import render, redirect
from employee.models import Employee
from django.http import HttpResponse
from employee.form import EmployeeForm
from employee.paginations import Pagination
from django.db.models import Q


# Create your views here.

def loop(request):
    for i in range(10):
        Employee.objects.create(e_id=i, e_name='het', e_designation='web_dev', e_email='het@gmail.com', e_contact='1234567890')
        
    return HttpResponse('<h1>done broooo</h1>')

def emp(request):  
    paginator = Pagination()
    last_page = Employee.objects.all().count() // 10 + 1
    employees, total_page, total_record = paginator.paginate(page=last_page)
    if total_page > last_page:
        last_page = last_page + 1  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                return redirect('/show/'+str(last_page)) 
            except ValueError:  
                print('oops....')
        return redirect("/show/"+str(last_page)) 
    else:  
        form = EmployeeForm()  
    return render(request,'employee/index.html',{'form': form})
  
def emp_show(request, page):  
    search = request.GET.get('search')
    if not search: 
        paginator = Pagination()
        employees, total_page, total_record = paginator.paginate(page=page)
        return render(request,"employee/show.html",{'employees':employees, 'current_page':page, "total_page":range(1,total_page+1), 'total_record':total_record})  
    else:
        employees = Employee.objects.filter(Q(e_name__istartswith=search) | Q(e_designation__istartswith=search) | Q(e_email__istartswith=search))
        return render(request,"employee/show.html",{'employees':employees, 'current_page':page})  
    

# def emp_edit(request, id):  
#     if request.method == 'POST':
#         return redirect('/show/')
#     employee = Employee.objects.get(id=id)  
#     return render(request,'employee/edit.html', {'employee':employee})  

def emp_update(request, id, page):  
    if request.method == 'POST':
        paginator = Pagination()
        employees, total_page, total_record = paginator.paginate(page=page)
        employee = Employee.objects.get(id=id)  
        form = EmployeeForm(request.POST, instance = employee)
        if form.is_valid():  
            form.save()  
            return redirect("/show/"+str(page))  
    else:
        employee = Employee.objects.get(id=id)  
        form = EmployeeForm(instance = employee)
        return render(request, 'employee/edit.html', {'form': form, 'employee': employee, 'current_page':page})  

def emp_delete(request, id, page):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    paginator = Pagination()
    employees, total_page, total_record = paginator.paginate(page=page)
    if total_page < page:
        page = page - 1
    print('total_page: ', total_page)
    return redirect('/show/'+str(page))  