# Generated by Django 4.1.2 on 2022-10-24 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.ImageField(upload_to='')),
                ('rarity', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
            ],
        ),
    ]