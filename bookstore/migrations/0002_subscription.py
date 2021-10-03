# Generated by Django 3.2 on 2021-05-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(max_length=50)),
                ('per', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('days', models.BigIntegerField()),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
