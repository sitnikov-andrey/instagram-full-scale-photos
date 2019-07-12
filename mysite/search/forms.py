from django import forms
 
class URLForm(forms.Form):
    URL = forms.CharField()