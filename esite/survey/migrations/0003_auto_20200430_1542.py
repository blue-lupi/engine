# Generated by Django 2.2.9 on 2020-04-30 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('survey', '0002_delete_surveyformsubmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='formfield',
            name='placeholder',
            field=models.CharField(blank=True, help_text='Placeholder value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='placeholder value'),
        ),
        migrations.AddField(
            model_name='formfield',
            name='title',
            field=models.CharField(blank=True, help_text='The title of the form field', max_length=255, null=True),
        ),
    ]
