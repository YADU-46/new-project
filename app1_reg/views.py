from django.shortcuts import render
from django.http import HttpResponse
from app1_reg.models import Student_details
# Create your views here.
# creating a three view pages
from app1_reg.forms import Reg
def home(request):
    # return HttpResponse('This is my home page')
    return render(request, 'app1_reg/home.html')

def reg(request):
    # return HttpResponse('This is my registration page')
    form = Reg()
    if request.method == 'POST':
        form = Reg(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("<h2 style = 'color:blue;'>Record inserted successfully</h2>")
        else:
            print("ERROR: FORM INVALID")
    return render(request, 'app1_reg/reg.html', {'form':form})

def report(request):
    std_details = Student_details.objects.order_by('std_name')
    std_details_dict= {'inserting_the_student_details':std_details}
    return render(request, 'app1_reg/report.html', context=std_details_dict)
