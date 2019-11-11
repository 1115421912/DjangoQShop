# Generated by Django 2.1.8 on 2019-11-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0002_auto_20191110_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='HarvestAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('gender', models.CharField(blank=True, max_length=4, null=True)),
                ('phone_number', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('default', models.CharField(default=0, max_length=4)),
            ],
        ),
    ]