# Generated by Django 3.2.7 on 2021-09-23 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='category',
            field=models.CharField(choices=[('Standalone', 'Standalone'), ('Community', 'Community')], max_length=255),
        ),
    ]
