# Generated by Django 5.0.6 on 2024-09-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(max_length=1000, upload_to=''),
        ),
    ]
