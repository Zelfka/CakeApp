# Generated by Django 4.1.3 on 2022-11-11 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='closed',
        ),
    ]
