# Generated by Django 3.0.9 on 2020-09-30 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videorequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videotitle',
            field=models.CharField(max_length=20),
        ),
    ]
