# Generated by Django 4.2.5 on 2023-11-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0033_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
