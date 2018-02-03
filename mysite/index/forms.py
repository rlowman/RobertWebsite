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
    # fieldData = None
    # def __init__(fieldData):
    #    fieldData = fieldData
    cellRow0Col0 = forms.CharField(max_length=1, required=False, widget=forms.TextInput(attrs={"size":"1", "value":"4"}))
    # cellRow0Col1 = forms.CharField(max_length=1, required=False, initial=fieldData[0][1], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow0Col2 = forms.CharField(max_length=1, required=False, initial=fieldData[0][2], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow0Col3 = forms.CharField(max_length=1, required=False, initial=fieldData[0][3], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow0Col4 = forms.CharField(max_length=1, required=False, initial=fieldData[0][4], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow0Col5 = forms.CharField(max_length=1, required=False, initial=fieldData[0][5], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow0Col6 = forms.CharField(max_length=1, required=False, initial=fieldData[0][6], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow0Col7 = forms.CharField(max_length=1, required=False, initial=fieldData[0][7], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow0Col8 = forms.CharField(max_length=1, required=False, initial=fieldData[0][8], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow1Col0 = forms.CharField(max_length=1, required=False, initial=fieldData[1][0], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow1Col1 = forms.CharField(max_length=1, required=False, initial=fieldData[1][1], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow1Col2 = forms.CharField(max_length=1, required=False, initial=fieldData[1][2], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow1Col3 = forms.CharField(max_length=1, required=False, initial=fieldData[1][3], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow1Col4 = forms.CharField(max_length=1, required=False, initial=fieldData[1][4], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow1Col5 = forms.CharField(max_length=1, required=False, initial=fieldData[1][5], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow1Col6 = forms.CharField(max_length=1, required=False, initial=fieldData[1][6], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow1Col7 = forms.CharField(max_length=1, required=False, initial=fieldData[1][7], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow1Col8 = forms.CharField(max_length=1, required=False, initial=fieldData[1][8], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow2Col0 = forms.CharField(max_length=1, required=False, initial=fieldData[2][0], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow2Col1 = forms.CharField(max_length=1, required=False, initial=fieldData[2][1], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow2Col2 = forms.CharField(max_length=1, required=False, initial=fieldData[2][2], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow2Col3 = forms.CharField(max_length=1, required=False, initial=fieldData[2][3], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow2Col4 = forms.CharField(max_length=1, required=False, initial=fieldData[2][4], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow2Col5 = forms.CharField(max_length=1, required=False, initial=fieldData[2][5], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow2Col6 = forms.CharField(max_length=1, required=False, initial=fieldData[2][6], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow2Col7 = forms.CharField(max_length=1, required=False, initial=fieldData[2][7], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow2Col8 = forms.CharField(max_length=1, required=False, initial=fieldData[2][8], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow3Col0 = forms.CharField(max_length=1, required=False, initial=fieldData[3][0], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow3Col1 = forms.CharField(max_length=1, required=False, initial=fieldData[3][1], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow3Col2 = forms.CharField(max_length=1, required=False, initial=fieldData[3][2], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow3Col3 = forms.CharField(max_length=1, required=False, initial=fieldData[3][3], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow3Col4 = forms.CharField(max_length=1, required=False, initial=fieldData[3][4], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow3Col5 = forms.CharField(max_length=1, required=False, initial=fieldData[3][5], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow3Col6 = forms.CharField(max_length=1, required=False, initial=fieldData[3][6], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow3Col7 = forms.CharField(max_length=1, required=False, initial=fieldData[3][7], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow3Col8 = forms.CharField(max_length=1, required=False, initial=fieldData[3][8], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow4Col0 = forms.CharField(max_length=1, required=False, initial=fieldData[4][0], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow4Col1 = forms.CharField(max_length=1, required=False, initial=fieldData[4][1], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow4Col2 = forms.CharField(max_length=1, required=False, initial=fieldData[4][2], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow4Col3 = forms.CharField(max_length=1, required=False, initial=fieldData[4][3], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow4Col4 = forms.CharField(max_length=1, required=False, initial=fieldData[4][4], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow4Col5 = forms.CharField(max_length=1, required=False, initial=fieldData[4][5], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow4Col6 = forms.CharField(max_length=1, required=False, initial=fieldData[4][6], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow4Col7 = forms.CharField(max_length=1, required=False, initial=fieldData[4][7], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow4Col8 = forms.CharField(max_length=1, required=False, initial=fieldData[4][8], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow5Col0 = forms.CharField(max_length=1, required=False, initial=fieldData[5][0], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow5Col1 = forms.CharField(max_length=1, required=False, initial=fieldData[5][1], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow5Col2 = forms.CharField(max_length=1, required=False, initial=fieldData[5][2], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow5Col3 = forms.CharField(max_length=1, required=False, initial=fieldData[5][3], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow5Col4 = forms.CharField(max_length=1, required=False, initial=fieldData[5][4], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow5Col5 = forms.CharField(max_length=1, required=False, initial=fieldData[5][5], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow5Col6 = forms.CharField(max_length=1, required=False, initial=fieldData[5][6], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow5Col7 = forms.CharField(max_length=1, required=False, initial=fieldData[5][7], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow5Col8 = forms.CharField(max_length=1, required=False, initial=fieldData[5][8], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow6Col0 = forms.CharField(max_length=1, required=False, initial=fieldData[6][0], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow6Col1 = forms.CharField(max_length=1, required=False, initial=fieldData[6][1], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow6Col2 = forms.CharField(max_length=1, required=False, initial=fieldData[6][2], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow6Col3 = forms.CharField(max_length=1, required=False, initial=fieldData[6][3], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow6Col4 = forms.CharField(max_length=1, required=False, initial=fieldData[6][4], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow6Col5 = forms.CharField(max_length=1, required=False, initial=fieldData[6][5], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow6Col6 = forms.CharField(max_length=1, required=False, initial=fieldData[6][6], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow6Col7 = forms.CharField(max_length=1, required=False, initial=fieldData[6][7], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow6Col8 = forms.CharField(max_length=1, required=False, initial=fieldData[6][8], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow7Col0 = forms.CharField(max_length=1, required=False, initial=fieldData[7][0], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow7Col1 = forms.CharField(max_length=1, required=False, initial=fieldData[7][1], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow7Col2 = forms.CharField(max_length=1, required=False, initial=fieldData[7][2], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow7Col3 = forms.CharField(max_length=1, required=False, initial=fieldData[7][3], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow7Col4 = forms.CharField(max_length=1, required=False, initial=fieldData[7][4], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow7Col5 = forms.CharField(max_length=1, required=False, initial=fieldData[7][5], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow7Col6 = forms.CharField(max_length=1, required=False, initial=fieldData[7][6], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow7Col7 = forms.CharField(max_length=1, required=False, initial=fieldData[7][7], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow7Col8 = forms.CharField(max_length=1, required=False, initial=fieldData[7][8], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow8Col0 = forms.CharField(max_length=1, required=False, initial=fieldData[8][0], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow8Col1 = forms.CharField(max_length=1, required=False, initial=fieldData[8][1], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow8Col2 = forms.CharField(max_length=1, required=False, initial=fieldData[8][2], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow8Col3 = forms.CharField(max_length=1, required=False, initial=fieldData[8][3], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow8Col4 = forms.CharField(max_length=1, required=False, initial=fieldData[8][4], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow8Col5 = forms.CharField(max_length=1, required=False, initial=fieldData[8][5], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow8Col6 = forms.CharField(max_length=1, required=False, initial=fieldData[8][6], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow8Col7 = forms.CharField(max_length=1, required=False, initial=fieldData[8][7], widget=forms.TextInput(attrs={"size":"1"}))
    # cellRow8Col8 = forms.CharField(max_length=1, required=False, initial=fieldData[8][8], widget=forms.TextInput(attrs={"size":"1"}))


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
