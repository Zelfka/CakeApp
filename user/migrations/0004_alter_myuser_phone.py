# Generated by Django 4.1.3 on 2022-11-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_myuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]