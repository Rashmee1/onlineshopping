# Generated by Django 4.0 on 2021-12-20 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.subcategory'),
        ),
    ]
