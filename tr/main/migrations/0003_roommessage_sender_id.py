# Generated by Django 2.2.7 on 2019-11-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_roommessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommessage',
            name='sender_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]