# Generated by Django 2.0.3 on 2018-04-29 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180429_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Imagen'),
        ),
    ]
