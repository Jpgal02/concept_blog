# Generated by Django 3.1.2 on 2020-11-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tentative_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
