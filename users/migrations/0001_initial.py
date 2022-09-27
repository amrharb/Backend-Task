# Generated by Django 4.1.1 on 2022-09-26 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_date', models.DateField(max_length=8)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.TextField()),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]
