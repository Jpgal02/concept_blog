# Generated by Django 3.1.2 on 2020-12-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_auto_20201208_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='efficacy_image',
            field=models.ImageField(blank=True, null=True, upload_to='efficacy_images/', verbose_name='효능/임상 이미지'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='title_images/', verbose_name='대표 이미지'),
        ),
    ]
