# Generated by Django 3.1.2 on 2020-11-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201108_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='export_country',
        ),
        migrations.AddField(
            model_name='category',
            name='export_country',
            field=models.CharField(default=1, help_text='수출가능 국가를 입력하세요.', max_length=50),
            preserve_default=False,
        ),
    ]
