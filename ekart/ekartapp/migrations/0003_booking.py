# Generated by Django 4.2 on 2023-04-19 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekartapp', '0002_productcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phn', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekartapp.productcard')),
            ],
        ),
    ]