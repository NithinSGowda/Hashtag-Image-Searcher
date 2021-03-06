# Generated by Django 3.0.2 on 2020-04-23 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200421_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedelement',
            name='image',
        ),
        migrations.RemoveField(
            model_name='feedelement',
            name='title',
        ),
        migrations.CreateModel(
            name='ImageTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.SearchTag')),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FeedElement')),
            ],
        ),
    ]
