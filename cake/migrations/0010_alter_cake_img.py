# Generated by Django 4.1.3 on 2022-11-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0009_cake_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='img',
            field=models.CharField(default='fox.png', max_length=200),
        ),
    ]
