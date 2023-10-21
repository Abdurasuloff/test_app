# Generated by Django 4.2.6 on 2023-10-17 11:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_test_pass_percentage_alter_test_end_date_checktest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checktest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checktests', to='main.test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 19, 11, 44, 24, 957011, tzinfo=datetime.timezone.utc), verbose_name='tugash sanasi'),
        ),
    ]
