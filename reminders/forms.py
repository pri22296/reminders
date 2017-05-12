from django.forms import ModelForm, ValidationError
from .models import Reminder
from datetime import date

class ReminderCreationForm(ModelForm):
    class Meta:
        model = Reminder
        fields = ('title','detail','date')

    def clean_date(self):
        data = self.cleaned_data['date']
        if data<date.today():
            raise ValidationError("Given Date has already passed!")
        return data
