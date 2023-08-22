from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class TicketStatus(models.TextChoices):
	TO_DO = 'To Do'
	IN_PROGRESS = 'In Progress'
	IN_REVIEW = 'In Review'
	DONE = 'Done'

class TicketDepartment(models.TextChoices):
	AC = 'AC'
	CARPENTRY = 'Carpentry'
	PLUMBING = 'Plumbing'
	ELECTRICAL='Electrical'
	WATER_MANAGEMENT='Water management'
	GIRLS_HOSTEL='Girls Hostel'
	BOYS_HOSTEL='Boys Hostel'



class Ticket(models.Model):
	title = models.CharField(max_length=100)
	assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
	status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
	department=models.CharField(max_length=25,choices=TicketDepartment.choices, default=TicketDepartment.AC)
	description = models.TextField()
	created_at = models.DateTimeField('created at', auto_now_add=True)
	updated_at = models.DateTimeField('updated at', auto_now=True)