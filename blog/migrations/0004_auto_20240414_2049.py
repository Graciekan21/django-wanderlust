# Generated by Django 3.2.25 on 2024-04-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_name_category_name_1'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-name_1']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.TextField(default='admin'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(choices=[('Travel Destinations', 'Travel Destinations'), ('Tourism', 'Tourism'), ('Politics', 'Politics'), ('Forestry', 'Forestry'), ('Cities', 'Cities')], default=1),
        ),
    ]
