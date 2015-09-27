from django_cron import CronJobBase, Schedule
from django.core.email import send_mail
from .models import Adherent
from django.utils import timezone

class RelanceAdherents(CronJobBase):
    RUN_EVERY_MINS = 120 #every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'adherents.relance'

    def do(self):
        now = timezone.now()
        adherents = Adherent.objects.filter( relance_date=now )

        for adherent in adherents.objects.all():

        #si adherent a une adresse email, on le relance
            if adherent.email != '':
                send_mail('subject', 'message', 'bureau@faimaison.net', ['gde@cosmogol.net'])

        
      
