# Generated by Django 4.2.20 on 2025-04-30 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_alter_siteinfo_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='slogan',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
