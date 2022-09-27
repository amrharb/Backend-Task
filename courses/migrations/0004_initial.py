# Generated by Django 4.1.1 on 2022-09-27 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'course',
                'ordering': ['name', '-description'],
            },
        ),
    ]
