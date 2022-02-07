# Generated by Django 2.2.10 on 2022-02-07 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_auto_20220207_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='surveys.Question'),
        ),
    ]
