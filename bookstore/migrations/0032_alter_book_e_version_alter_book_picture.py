# Generated by Django 4.2.5 on 2023-11-30 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0031_alter_book_e_version_alter_book_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='e_version',
            field=models.FileField(blank=True, max_length=150, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
