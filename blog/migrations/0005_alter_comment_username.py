# Generated by Django 3.2.25 on 2024-04-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20240414_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(default='admin', max_length=80),
        ),
    ]
