# Generated by Django 4.1 on 2022-08-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
