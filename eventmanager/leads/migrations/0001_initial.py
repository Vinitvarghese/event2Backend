# Generated by Django 3.0.2 on 2020-02-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('tin_number', models.IntegerField()),
            ],
        ),
    ]
