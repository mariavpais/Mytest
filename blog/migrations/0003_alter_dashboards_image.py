# Generated by Django 3.2.11 on 2022-02-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220226_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboards',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog_images'),
        ),
    ]
