# Generated by Django 3.1.4 on 2022-06-26 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220626_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='referaluser',
            name='refer_by_without_register',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]