# Generated by Django 2.2.1 on 2020-02-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]
