# Generated by Django 4.2.5 on 2023-09-13 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
