# Generated by Django 3.1.2 on 2020-12-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20201208_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='efficacy_image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to='', verbose_name='효능/임상 이미지'),
        ),
    ]