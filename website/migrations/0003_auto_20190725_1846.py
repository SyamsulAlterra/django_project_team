# Generated by Django 2.2.3 on 2019-07-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190725_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='maps',
            field=models.TextField(help_text='Insert html script from google maps', max_length=500),
        ),
    ]