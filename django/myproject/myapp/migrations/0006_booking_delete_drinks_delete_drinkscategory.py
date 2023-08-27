# Generated by Django 4.2.2 on 2023-08-27 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_prince_drinks_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('guest_count', models.IntegerField()),
                ('reservation_time', models.DateField(auto_now=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Drinks',
        ),
        migrations.DeleteModel(
            name='DrinksCategory',
        ),
    ]
