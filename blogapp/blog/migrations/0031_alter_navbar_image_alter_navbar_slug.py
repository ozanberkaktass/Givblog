# Generated by Django 4.0.6 on 2022-07-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_blog_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='image',
            field=models.ImageField(null=True, upload_to='blogs'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
