# Generated by Django 4.0 on 2021-12-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='subtitle',
            field=models.CharField(default=1, max_length=300),
        ),
    ]