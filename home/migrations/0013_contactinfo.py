# Generated by Django 4.0 on 2021-12-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_item_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('phone', models.TextField()),
            ],
        ),
    ]
