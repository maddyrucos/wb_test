# Generated by Django 5.2.3 on 2025-06-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('nm_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('price_basic', models.FloatField()),
                ('price_basic_rub', models.FloatField()),
                ('price_total', models.FloatField()),
                ('price_total_rub', models.FloatField()),
                ('rating', models.FloatField()),
                ('feedbacks', models.IntegerField()),
            ],
        ),
    ]
