from django import forms
from django.core import validators
from first_app.models import User
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    varify_email = forms.EmailField(label="Enter your email again:")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data.get("email",None)
        vmail = all_clean_data.get("verify_email",None)

        if email != vmail:
            raise forms.ValidationError('Emails are not the same')


class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
