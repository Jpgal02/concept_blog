# Generated by Django 3.1.2 on 2020-11-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20201111_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='efficacy_image',
            field=models.ImageField(default='media/default_image.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_image',
            field=models.ImageField(default='media/default_image.jpg', upload_to=''),
        ),
    ]