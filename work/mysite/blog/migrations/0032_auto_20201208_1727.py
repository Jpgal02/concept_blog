# Generated by Django 3.1.2 on 2020-12-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20201208_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='efficacy_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='효능/임상 이미지'),
        ),
    ]
