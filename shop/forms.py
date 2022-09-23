from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control mt-1'
            self.fields['name'].widget.attrs['placeholder'] = 'نام'
            self.fields['email'].widget.attrs['placeholder'] = 'ایمیل'
            self.fields['subject'].widget.attrs['placeholder'] = 'موضوع'
            self.fields['message'].widget.attrs['placeholder'] = 'پیغام'

            
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'message']

