# Generated by Django 3.0.2 on 2020-04-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_searchtag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchtag',
            name='id',
        ),
        migrations.AlterField(
            model_name='searchtag',
            name='tag',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
