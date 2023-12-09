# Generated by Django 5.0 on 2023-12-09 00:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_alter_item_buyer'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boughtitem', to='users.myuser'),
        ),
        migrations.AlterField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solditem', to='users.myuser'),
        ),
    ]
