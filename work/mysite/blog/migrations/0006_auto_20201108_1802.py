# Generated by Django 3.1.2 on 2020-11-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='efficacy_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='export_country',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='main_benefit',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
