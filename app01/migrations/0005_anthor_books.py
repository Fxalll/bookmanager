# Generated by Django 3.1.6 on 2021-02-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_anthor'),
    ]

    operations = [
        migrations.AddField(
            model_name='anthor',
            name='books',
            field=models.ManyToManyField(to='app01.Book'),
        ),
    ]
