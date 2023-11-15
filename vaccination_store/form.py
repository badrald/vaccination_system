from django import forms
from .models import JobPlace,Vaccination

class JobPlaceForm(forms.ModelForm):
    class Meta:
        model = JobPlace
        fields="__all__"



class VaccinationForm(forms.ModelForm):
    class Meta:
        model= Vaccination
        fields="__all__"