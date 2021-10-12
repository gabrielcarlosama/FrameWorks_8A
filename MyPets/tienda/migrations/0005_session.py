# Generated by Django 3.2.7 on 2021-10-09 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_auto_20211009_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('delated_at', models.DateTimeField()),
            ],
        ),
    ]
