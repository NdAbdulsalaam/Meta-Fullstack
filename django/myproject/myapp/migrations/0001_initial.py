# Generated by Django 4.2.2 on 2023-08-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('MemberID', models.IntegerField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('DateOfBirth', models.DateField()),
                ('Joined', models.DateTimeField()),
            ],
        ),
    ]
