# Generated by Django 3.1.1 on 2020-09-25 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200925_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orginal_bag',
            new_name='original_bag',
        ),
    ]
