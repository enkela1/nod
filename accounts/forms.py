from django import forms

class SignUpForm(forms.Form): 
    name = forms.CharField(label="Name", max_length=80)
    username = forms.CharField(label="Username", max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    agree_to_terms = forms.BooleanField(
        label="I accept the Terms & Conditions and Privacy Policy, including the no-harrasment rules",
        required=True,
        error_messages={'required': 'You must accept the terms to proceed.'}
    )