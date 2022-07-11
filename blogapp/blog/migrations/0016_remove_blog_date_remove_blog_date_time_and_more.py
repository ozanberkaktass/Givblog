# Generated by Django 4.0.4 on 2022-06-28 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_blog_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='time',
        ),
        migrations.AddField(
            model_name='blog',
            name='contact_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Conversation Time'),
            preserve_default=False,
        ),
    ]