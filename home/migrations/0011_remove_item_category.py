# Generated by Django 4.0 on 2021-12-21 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_category_rank_item_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
    ]
