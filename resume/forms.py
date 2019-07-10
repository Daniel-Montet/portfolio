from django import forms

class MailMe(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Name'
                }
                ))
    email = forms.EmailField(widget=forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Email'
                }
                ))
    message = forms.CharField(widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols':'30',
                    'rows':'5',
                    'placeholder': 'Your Message'
                }
                ))