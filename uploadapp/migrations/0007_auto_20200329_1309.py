# Generated by Django 2.2.1 on 2020-03-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0006_auto_20200329_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]