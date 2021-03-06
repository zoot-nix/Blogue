# Generated by Django 4.0.2 on 2022-03-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogueApp', '0006_rename_contact_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/blogueApp/images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/blogueApp/images/'),
        ),
    ]
