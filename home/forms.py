from django import forms
from .models import AboutUser


class AboutForm(forms.ModelForm):

    class Meta:
        model = AboutUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-input rounded-0'
