from django import forms

class RotaluclacForm(forms.Form):
    CHOICES = [('binary','Binary'),
               ('octal','Octal'),
               ('decimal','Decimal'),
               ('hexadecimal', 'Hexadecimal')]
    base = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    equation = forms.CharField()
