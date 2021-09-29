# Generated by Django 3.2.7 on 2021-09-29 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ease_app', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.TextField(default='blank message', max_length=5000),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='blank', max_length=100),
        ),
    ]