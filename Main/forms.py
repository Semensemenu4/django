from django import forms

class CoinForm(forms.Form):
    date = forms.DateField()

    def date_coin(self):
        new_date = self.clean_date['date']
        return new_date
