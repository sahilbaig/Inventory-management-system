# Generated by Django 4.0.5 on 2023-05-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='name',
            field=models.CharField(default='transaction_name', max_length=100),
        ),
    ]
