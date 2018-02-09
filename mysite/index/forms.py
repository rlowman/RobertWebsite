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

class SodokuBoard(forms.Form):
    # TODO: Make loop work to avoid creating 81 input forms
    # board = [[]*9 for _ in range(9)]
    # for x in range(8):
    #     for y in range(8):
    #         board[x][y]
    CHOICES = [('backtracking', 'Backtracking')]

    algorithm = forms.CharField(label = "Select the solving algorithm",
                                widget = forms.Select(choices = CHOICES))
    cellRow0Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow0Col1 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow0Col2 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow0Col3 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow0Col4 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow0Col5 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow0Col6 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow0Col7 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow0Col8 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow1Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow1Col1 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow1Col2 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow1Col3 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow1Col4 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow1Col5 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow1Col6 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow1Col7 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow1Col8 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow2Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow2Col1 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow2Col2 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow2Col3 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow2Col4 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow2Col5 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow2Col6 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow2Col7 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow2Col8 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow3Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow3Col1 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow3Col2 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow3Col3 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow3Col4 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow3Col5 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow3Col6 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow3Col7 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow3Col8 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow4Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow4Col1 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow4Col2 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow4Col3 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow4Col4 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow4Col5 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow4Col6 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow4Col7 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow4Col8 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow5Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow5Col1 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow5Col2 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow5Col3 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow5Col4 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow5Col5 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow5Col6 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow5Col7 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow5Col8 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow6Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow6Col1 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow6Col2 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow6Col3 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow6Col4 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow6Col5 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow6Col6 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow6Col7 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow6Col8 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow7Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow7Col1 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow7Col2 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow7Col3 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow7Col4 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow7Col5 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow7Col6 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow7Col7 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow7Col8 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow8Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow8Col1 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow8Col2 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow8Col3 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow8Col4 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow8Col5 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow8Col6 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow8Col7 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))
    cellRow8Col8 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1"}))

# class CaeserCipherForm(forms.Form):
#     FUNCTIONCHOICES = [('encrypt', 'Encrypt'),
#                        ('decrypt', 'Decrypt')]
#     function = forms.CharField(widget = forms.Select(choices = FUNCTIONCHOICES))
#     text = forms.CharField(widget = forms.TextInput(attrs={
#         "placeholder": "Plain Text"
#     }))
#     key = forms.CharField(widget = forms.TextInput(attrs={
#         "placeholder": "Key"
#     }))
