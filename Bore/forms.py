from django import forms

class Activity(forms.Form):
    choices = [
        ("", "--------"),
        ("education","Education"),
        ("recreational","Recreation"),
        ("social","Social"),
        ("diy","DIY"),
        ("charity","Charity"),
        ("cooking","Cooking"),
        ("relaxation","Relaxation"),
        ("music","Music"),
        ("busywork","Busywork")
    ]
    type = forms.ChoiceField(choices=choices, required=False)
    participant = forms.FloatField(label="Participant Number", help_text="Number from 0 to n", required=False)
    accessibility = forms.FloatField(help_text="Possibility of the activity [0.1 to 1.0]", required=False)
    price = forms.FloatField(help_text="A factor describing the cost of the event."
                                           "Between 0 and 1.  0 fo free", required=False)


class NumberTriviaForm(forms.Form):
    CHOICES = [
        ("", "------"),
        ("trivia", "Trivia"),
        ("math", "Math"),
        ("date", "Date"),
        ("year", "Year"),
    #("random", "Random")
    ]
    type = forms.ChoiceField(choices=CHOICES)
    number = forms.CharField(help_text="Date should be in MM/DD format")

    def clean(self, *args,**kwargs):
        type = self.cleaned_data.get("type")
        number = self.cleaned_data.get("number")
        if type != "Date" and "/" in number:
            raise forms.ValidationError("Choose Date type for this format")
