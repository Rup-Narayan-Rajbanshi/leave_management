# Generated by Django 3.2.7 on 2021-10-01 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20211001_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaveapproval',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='leaveapproval',
            name='approval_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('YES', 'Approved'), ('NO', 'Not Approved')], default='PENDING', max_length=15),
        ),
    ]
