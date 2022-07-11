# Generated by Django 4.0.4 on 2022-06-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
    ]