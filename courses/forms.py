from django import forms
from django.core.exceptions import ValidationError

def validate_description_length(description):
    length=len(description)
    if(length<5 or length>100):
        raise ValidationError((
            "The length of the description must be between 5 and 100 characters"),
            code="invalid_description",
        )
    return description

class CoursesForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=100)
    description = forms.CharField(validators=[validate_description_length])