# Generated by Django 5.1.4 on 2024-12-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveryapp', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='name',
            field=models.CharField(default=0.0, max_length=50),
            preserve_default=False,
        ),
    ]