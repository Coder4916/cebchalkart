# Generated by Django 3.2.25 on 2024-06-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0011_alter_review_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
