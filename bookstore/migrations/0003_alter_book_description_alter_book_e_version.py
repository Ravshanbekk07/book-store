# Generated by Django 4.2.5 on 2023-11-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='book',
            name='e_version',
            field=models.FileField(blank=True, max_length=150, upload_to='documents/'),
        ),
    ]