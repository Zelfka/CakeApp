# Generated by Django 4.1.3 on 2022-11-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
