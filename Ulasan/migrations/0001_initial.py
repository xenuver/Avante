# Generated by Django 3.2.16 on 2023-05-09 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Produk', '0002_auto_20230509_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ulasan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isi_ulasan', models.TextField()),
                ('bintang_ulasan', models.IntegerField()),
                ('Produk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produk.produk')),
                
            ],
        ),
    ]
