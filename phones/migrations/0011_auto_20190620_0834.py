# Generated by Django 2.1.1 on 2019-06-20 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0010_auto_20190620_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='pixels',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='phone',
            name='ram',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='phone',
            name='op_s',
            field=models.CharField(choices=[('windows', 'windows'), ('android', 'android'), ('ios', 'ios')], max_length=50),
        ),
        migrations.AlterField(
            model_name='prod',
            name='feature',
            field=models.CharField(blank=True, default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='prod',
            name='phone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='features', to='phones.Phone'),
        ),
    ]