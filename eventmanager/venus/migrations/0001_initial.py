# Generated by Django 3.0.2 on 2020-02-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_title', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=30)),
                ('event_date', models.DateField()),
                ('description', models.CharField(max_length=300)),
                ('co_ordinate_x', models.CharField(max_length=200)),
                ('co_ordinate_y', models.CharField(max_length=200)),
                ('venu_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
