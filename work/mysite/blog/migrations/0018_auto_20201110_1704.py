# Generated by Django 3.1.2 on 2020-11-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20201110_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tentative_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
