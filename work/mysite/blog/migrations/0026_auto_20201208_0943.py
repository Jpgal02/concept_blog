# Generated by Django 3.1.2 on 2020-12-08 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_post_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='컨셉명'),
        ),
    ]