# Generated by Django 3.2 on 2021-04-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='157-1579943_no-profile-picture-round', upload_to='products'),
        ),
    ]
