# Generated by Django 4.1.3 on 2022-11-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0004_remove_sponge_cake_cake_sponges'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cream',
            name='fruit',
        ),
        migrations.DeleteModel(
            name='PriceList',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='cream',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='decorations',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='fruit',
        ),
        migrations.RemoveField(
            model_name='cake',
            name='sponges',
        ),
        migrations.AddField(
            model_name='cake',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='cake',
            name='eggs_free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cake',
            name='milk_free',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Cream',
        ),
        migrations.DeleteModel(
            name='Decoration',
        ),
        migrations.DeleteModel(
            name='Fruit',
        ),
        migrations.DeleteModel(
            name='Sponge',
        ),
    ]
