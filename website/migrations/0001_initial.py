# Generated by Django 2.2.3 on 2019-07-25 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Insert place name', max_length=255)),
                ('description', models.TextField(help_text='Insert place descriptions', max_length=1000)),
                ('maps', models.CharField(help_text='Insert html script from google maps', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=500)),
                ('place_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Places')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_url', models.CharField(max_length=255)),
                ('place_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Places')),
            ],
        ),
    ]
