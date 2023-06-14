from socket import fromshare
from django import forms


class HtmlForm(forms.Form):
    name = forms.CharField(lable='Город')
