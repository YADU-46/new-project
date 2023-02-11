from django import forms
from student_details.models import Marks

class Marks_form(forms.ModelForm):
    class Meta:
        model = Marks
        fields = "__all__"
