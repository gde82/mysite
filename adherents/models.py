from django.db import models
from django.utils import timezone
#from django.core.exceptions import ValidationError
import datetime

# Create your models here.

class Adherents(models.Model):
    now = timezone.now()
    next_year = now + datetime.timedelta(days=365)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    join_date = models.DateTimeField('join date', default=now)
    relance_date = models.DateTimeField('relance date', default=next_year)

#    def clean_relance_date(self):
#        date_relance = self_cleaned_data['relance_date']
#        if date_relance < self.join_date:
#            return ValidationError('n\'est pas une bonne date')

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def must_rejoin(self):
        return now >= self.relance_date 
