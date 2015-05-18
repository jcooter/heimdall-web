from django.db import models
from django.conrib.auth.models import User

class Page(models.Model):
    INFORMATIONAL = 'INFO'
    WARNING = 'WARN'
    CRITICAL = 'CRIT'
    SEVERITY_CHOICES = (
        (INFORMATIONAL, 'Informational'),
        (WARNING, 'Warning'),
        (CRITICAL, 'Critical'),
    )

    submit_date = models.DateTimeField('date submitted')
    to = models.ForeignKey(User)
    from = models.ForeignKey(User)
    short_message = models.CharField('short message', max_length=80)
    long_message = models.TextField('full message')
    severity = models.CharField(max_length=4, choices=SEVERITY_CHOICES, default=INFORMATIONAL)
    hostname = models.CharField(max_length=45, blank=True)
    ticket_number = models.PositiveIntegerField('ticket number', blank=True, null=True)

class Message(models.Model):
    GENERATING = 'GEN'
    DISPATCHED = 'DISP'
    SENT = 'SENT'
    FAILED = 'FAIL'
    RETRYING = 'RTRY'
    STATE_CHOICES = (
        (GENERATING, 'Generating'),
        (DISPATCHED, 'Dispatched'),
        (SENT, 'Sent'),
        (FAILED, 'Failed'),
	(RETRYING, 'Retrying'),
    )

    page = models.ForeignKey('Page')
    generate_date = models.DateTimeField('date generated')
    type = models.CharField(max_length=16)
    to = models.CharField('to address', max_length=45)
    state = models.CharField('status', max_length=4, choices=STATE_CHOICES, default=GENERATING)
    failed_count = models.PositiveSmallIntegerField('failed attempts')
    sent_date = models.DateTimeField('date sent')
