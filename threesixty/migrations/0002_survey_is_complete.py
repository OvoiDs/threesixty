# Generated by Django 2.0.2 on 2018-02-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threesixty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='is_complete',
            field=models.BooleanField(default=False, help_text='Will show results and reject further answers.', verbose_name='is complete'),
        ),
    ]
