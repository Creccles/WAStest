# Generated by Django 2.2 on 2022-03-22 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desc',
            new_name='description',
        ),
    ]