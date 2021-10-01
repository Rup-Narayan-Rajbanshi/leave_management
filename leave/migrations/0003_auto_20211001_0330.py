# Generated by Django 3.2.7 on 2021-10-01 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_leaveapproval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='approval_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('YES', 'Approved'), ('NO', 'Not Approved')], default='PENDING', max_length=15),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='leave_type',
            field=models.CharField(choices=[('FULL', 'Full'), ('HALF', 'Half')], default='FULL', max_length=15),
        ),
    ]
