from django import forms
from app1_reg.models import Student_details
class Reg(forms.ModelForm):
    class Meta:
        model = Student_details
        fields = "__all__"
