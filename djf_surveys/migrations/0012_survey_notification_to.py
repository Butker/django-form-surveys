# Generated by Django 4.1.13 on 2024-02-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djf_surveys', '0011_alter_question_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='notification_to',
            field=models.TextField(blank=True, help_text='Enter your email to be notified when the form is submitted', null=True, verbose_name='Notification To'),
        ),
    ]
