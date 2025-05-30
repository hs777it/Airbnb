# Generated by Django 4.2.20 on 2025-04-30 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_alter_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='places/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(default='', upload_to='property/'),
            preserve_default=False,
        ),
    ]
