# Generated by Django 3.1.2 on 2020-11-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tentative_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='inci_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]