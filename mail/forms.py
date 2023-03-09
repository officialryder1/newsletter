from django import forms
from . models import Subcriber, MailMessage


class Subscriberform(forms.ModelForm):
    class Meta:
        model = Subcriber
        fields = ['email',]

class MailMassageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = "__all__"