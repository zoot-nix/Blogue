# Generated by Django 3.2.8 on 2022-02-01 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogueApp', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]