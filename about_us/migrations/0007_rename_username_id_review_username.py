# Generated by Django 3.2.25 on 2024-06-24 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0006_review_username_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='username_id',
            new_name='username',
        ),
    ]
