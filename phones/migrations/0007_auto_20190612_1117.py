# Generated by Django 2.1.5 on 2019-06-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_auto_20190612_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='op_s',
            field=models.CharField(choices=[('android', 'android'), ('ios', 'ios'), ('windows', 'windows')], max_length=50),
        ),
    ]
