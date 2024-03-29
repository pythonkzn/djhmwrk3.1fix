# Generated by Django 2.1.5 on 2019-06-11 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_auto_20190611_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField()),
                ('feature_one', models.TextField()),
                ('feature_two', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='phone',
            name='cost',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='op_s',
            field=models.CharField(choices=[('windows', 'windows'), ('ios', 'ios'), ('android', 'android')], max_length=50),
        ),
        migrations.AddField(
            model_name='phone',
            name='prod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='phones.Prod'),
        ),
    ]
