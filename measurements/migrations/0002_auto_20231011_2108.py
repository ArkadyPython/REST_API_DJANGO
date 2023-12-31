# Generated by Django 3.1.2 on 2023-10-11 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='project',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='value',
        ),
        migrations.AddField(
            model_name='measurement',
            name='temperature',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='measurements.sensor'),
            preserve_default=False,
        ),
    ]
