# Formulario Django
from django import forms
from PCs.models import Desktop



class DesktopModelForm(forms.ModelForm):

    class Meta:
        model = Desktop
        fields = '__all__'