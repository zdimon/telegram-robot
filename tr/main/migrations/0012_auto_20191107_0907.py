# Generated by Django 2.2.7 on 2019-11-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20191107_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='alias',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
