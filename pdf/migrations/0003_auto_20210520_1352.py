# Generated by Django 3.2 on 2021-05-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0002_profile_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='profile',
            name='university',
            field=models.TextField(max_length=500),
        ),
    ]