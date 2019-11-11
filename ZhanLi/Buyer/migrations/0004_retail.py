# Generated by Django 2.1.8 on 2019-11-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0003_harvestaddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=32)),
                ('r_introduction', models.CharField(max_length=32)),
                ('r_picture', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
    ]
