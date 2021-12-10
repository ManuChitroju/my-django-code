from django import forms
import datetime


class puzzle_form(forms.Form):
        number=forms.IntegerField(label='Enter a positive odd number')
