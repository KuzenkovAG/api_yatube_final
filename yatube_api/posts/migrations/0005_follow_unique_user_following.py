# Generated by Django 3.2.16 on 2023-03-24 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230323_2101'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_user_following'),
        ),
    ]
