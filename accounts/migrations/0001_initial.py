# Generated by Django 3.2 on 2021-05-23 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsciption', models.CharField(max_length=20)),
                ('cart', models.ManyToManyField(related_name='bookcart', to='bookstore.Book')),
                ('owned', models.ManyToManyField(related_name='mybook', to='bookstore.Book')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wishlist', models.ManyToManyField(related_name='wishbook', to='bookstore.Book')),
            ],
        ),
    ]
