# Generated by Django 4.2.4 on 2023-08-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('In Review', 'In Review'), ('Done', 'Done')], default='To Do', max_length=25),
        ),
    ]
    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='department',
            field=models.CharField(choices=[('ac', 'AC'), ('carpentry', 'Carpentry'), ('plumbing', 'Pluming'), ('electrical', 'Electrical'),('water_management','Water management'),('girls hostel','Girls Hostel')], default='ac', max_length=25),
        ),
    ]
