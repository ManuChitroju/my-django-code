# Generated by Django 3.2.8 on 2021-12-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tambola2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('str1', models.CharField(max_length=128)),
                ('random_number', models.PositiveIntegerField()),
            ],
        ),
    ]