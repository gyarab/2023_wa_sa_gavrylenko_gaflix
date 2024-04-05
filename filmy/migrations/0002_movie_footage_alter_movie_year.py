# Generated by Django 5.0.3 on 2024-04-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='footage',
            field=models.PositiveSmallIntegerField(blank=True, help_text='in minutes', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
