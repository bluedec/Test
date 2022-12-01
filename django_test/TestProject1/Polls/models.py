import datetime
from django.utils import timezone
from django.db import models 


class Question(models.Model):
    text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def recently_published(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=6)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('choice_text', max_length=200)
    votes = models.IntegerField('votos!', default=0)

    def __str__(self):
        return self.choice_text
