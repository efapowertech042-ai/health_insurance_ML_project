from django import forms

SEX_CHOICES = [("female", "Female"), ("male", "Male")]
SMOKER_CHOICES = [("no", "No"), ("yes", "Yes")]
REGION_CHOICES = [
    ("northeast", "Northeast"),
    ("northwest", "Northwest"),
    ("southeast", "Southeast"),
    ("southwest", "Southwest"),
]


class ChargesPredictionForm(forms.Form):
    age = forms.IntegerField(
        min_value=18, max_value=100,
        widget=forms.NumberInput(attrs={"class": "form-input"}),
        help_text="Training data covered ages 18-64; predictions outside that range are extrapolated.",
    )
    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.Select(attrs={"class": "form-input"}),
    )
    bmi = forms.FloatField(
        min_value=10.0, max_value=70.0,
        widget=forms.NumberInput(attrs={"class": "form-input", "step": "0.1"}),
        help_text="Training data covered BMI roughly 15-53.",
    )
    children = forms.IntegerField(
        min_value=0, max_value=10,
        widget=forms.NumberInput(attrs={"class": "form-input"}),
    )
    smoker = forms.ChoiceField(
        choices=SMOKER_CHOICES,
        widget=forms.Select(attrs={"class": "form-input"}),
    )
    region = forms.ChoiceField(
        choices=REGION_CHOICES,
        widget=forms.Select(attrs={"class": "form-input"}),
    )
