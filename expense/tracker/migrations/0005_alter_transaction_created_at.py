# Generated by Django 5.1.3 on 2024-12-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_remove_transaction_id_alter_transaction_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
