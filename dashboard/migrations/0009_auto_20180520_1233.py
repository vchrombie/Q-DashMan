# Generated by Django 2.0 on 2018-05-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_backends_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backends',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
