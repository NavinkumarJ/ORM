# Generated by Django 4.2.6 on 2023-10-31 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(help_text='Player ID', max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
