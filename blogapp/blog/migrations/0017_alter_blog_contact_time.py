# Generated by Django 4.0.4 on 2022-06-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_blog_date_remove_blog_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contact_time',
            field=models.TimeField(null='h:m:s'),
        ),
    ]
