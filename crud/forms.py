from django import forms
from .models import Curator


class CuratorsForm(forms.ModelForm):

    class Meta:
        model = Curator
        fields = ('name', 'surname', 'description',)
