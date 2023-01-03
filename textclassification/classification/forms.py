from django import forms

class NameForm(forms.Form):
    text_to_classify = forms.CharField(widget=forms.Textarea,label='Text to Classify', max_length=1000)