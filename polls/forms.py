from django import forms
  
class UserForm(forms.Form):
    sentence = forms.CharField(label='sentence', max_length=1000, widget=forms.Textarea)
