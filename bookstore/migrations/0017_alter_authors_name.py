# Generated by Django 4.1.7 on 2023-11-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0016_alter_authors_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]