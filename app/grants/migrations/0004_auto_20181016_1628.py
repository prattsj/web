# Generated by Django 2.1.2 on 2018-10-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0003_auto_20181010_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='block_number',
            field=models.CharField(default=0, max_length=9),
        ),
        migrations.AddField(
            model_name='subscription',
            name='period_seconds',
            field=models.DecimalField(decimal_places=0, default=2592000, max_digits=50),
        ),
        migrations.AlterField(
            model_name='grant',
            name='network',
            field=models.CharField(default='mainnet', max_length=8),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='network',
            field=models.CharField(default='mainnet', max_length=8),
        ),
    ]
