# Generated by Django 5.1.6 on 2025-03-14 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.PositiveIntegerField(),
        ),
    ]
