# Generated by Django 4.2.5 on 2023-11-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0009_rename_firstname_authors_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='bookstore.authors'),
        ),
    ]
