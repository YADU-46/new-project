from django.shortcuts import render
from student_details.forms import Marks_form
from django.http import HttpResponse
# Create your views here.

def Marks(response):
    form_m = Marks_form()
    if response.method == 'POST':
        form_m = Marks_form(response.POST)
        if form_m.is_valid():
            form_m.save(commit=True)
            return HttpResponse("<h2 style = 'color:blue;'>Record inserted successfully</h2>")
        else:
            print("ERROR: FORM INVALID")
    return render(response,'app1_reg/marks.html', context= dict({'form_m': form_m}))

