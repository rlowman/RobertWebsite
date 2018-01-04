from django import forms

class RotaluclacForm(forms.Form):
    CHOICES = [('binary','Binary'),
               ('octal','Octal'),
               ('decimal','Decimal'),
               ('hexadecimal', 'Hexadecimal')]
    NOTATIONCHOICES = [('polish', 'Polish Notation'),
                       ('reverse', 'Reverse Polish Notation')]
    notation = forms.CharField(label = "Select the Notation: ",
                               widget = forms.Select(choices = NOTATIONCHOICES))
    base = forms.ChoiceField(label = "Select Base for Answer: ", choices=CHOICES,
                             initial = 'decimal',
                             widget=forms.RadioSelect())
    equation = forms.CharField(widget = forms.TextInput(attrs={
        "placeholder": "Enter Equation Here",
        "size" : "40" }))
