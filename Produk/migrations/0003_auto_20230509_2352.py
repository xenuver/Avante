# Generated by Django 3.2.16 on 2023-05-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produk', '0002_auto_20230509_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategoriproduk',
            name='id',
        ),
        migrations.AddField(
            model_name='kategoriproduk',
            name='id_kategori',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
