# Generated by Django 3.2.12 on 2022-06-06 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_email_contact_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
    ]
