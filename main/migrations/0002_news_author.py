# Generated by Django 4.1.7 on 2023-02-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default='Anonymous', max_length=200),
        ),
    ]