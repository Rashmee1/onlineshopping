# Generated by Django 4.0 on 2021-12-28 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_remove_cart_total'),
        ('checkout', '0002_delete_totalcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Totalcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('carts', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
            ],
        ),
    ]
