# Generated by Django 4.1.3 on 2022-11-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0003_pricelist_rename_flour_qt_sponge_flour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponge',
            name='cake',
        ),
        migrations.AddField(
            model_name='cake',
            name='sponges',
            field=models.ManyToManyField(to='cake.sponge'),
        ),
    ]
