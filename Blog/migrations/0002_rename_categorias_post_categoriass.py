# Generated by Django 4.0.4 on 2022-07-24 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categorias',
            new_name='categoriass',
        ),
    ]
