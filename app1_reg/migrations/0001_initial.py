# Generated by Django 4.1.5 on 2023-02-03 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.CharField(max_length=260, unique=True)),
                ('std_name', models.CharField(max_length=260)),
                ('std_age', models.PositiveIntegerField()),
                ('std_gender', models.CharField(max_length=200)),
                ('std_phone', models.PositiveSmallIntegerField(unique=True)),
                ('std_email', models.EmailField(max_length=260, unique=True)),
            ],
        ),
    ]