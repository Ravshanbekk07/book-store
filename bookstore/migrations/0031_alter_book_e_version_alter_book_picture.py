# Generated by Django 4.2.5 on 2023-11-29 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0030_alter_book_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='e_version',
            field=models.FileField(blank=True, max_length=150, null=True, upload_to='medias/documents/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='medias/pictures/'),
        ),
    ]