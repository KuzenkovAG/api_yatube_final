# Generated by Django 3.2.16 on 2023-03-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230323_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]