# Generated by Django 5.0.4 on 2024-05-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catagory',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='catagory',
            name='image',
        ),
        migrations.AddField(
            model_name='catagory',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
