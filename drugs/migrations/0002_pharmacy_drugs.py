# Generated by Django 3.0 on 2019-12-14 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='drugs',
            field=models.ManyToManyField(to='drugs.Drugs'),
        ),
    ]
