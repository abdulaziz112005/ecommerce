# Generated by Django 3.1.4 on 2020-12-24 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attributes',
            options={'verbose_name': 'Attributlar', 'verbose_name_plural': 'Attributlar'},
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name': 'Produkt turlari', 'verbose_name_plural': 'Produkt  turlari'},
        ),
        migrations.AlterModelOptions(
            name='values',
            options={'verbose_name': 'Qiymatlar', 'verbose_name_plural': 'Qiymatlar'},
        ),
    ]
