from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your name',
            'class': 'form-control'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'class': 'form-control'
        })
    )
    
    subject = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'form-control'
        })
    )
    
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Your message',
            'rows': 5,
            'class': 'form-control'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'contact-form'
        self.helper.add_input(Submit('submit', 'Send Message', css_class='btn-primary'))