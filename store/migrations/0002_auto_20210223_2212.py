# Generated by Django 3.1.6 on 2021-02-23 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodcut',
            name='description',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='prodcut',
            name='image',
            field=models.ImageField(upload_to='uploads/products/'),
        ),
    ]
