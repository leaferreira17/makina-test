# Generated by Django 5.0 on 2023-12-08 18:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold_item', to='users.myuser'),
        ),
        migrations.AlterField(
            model_name='item',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bought_item', to='users.myuser'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
