# Generated by Django 4.1.3 on 2022-12-05 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_alter_staff_password_alter_staff_pho'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='pho',
            new_name='phno',
        ),
    ]