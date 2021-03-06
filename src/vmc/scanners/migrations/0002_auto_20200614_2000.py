# Generated by Django 2.2.13 on 2020-06-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='config',
            name='error_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='config',
            name='last_success_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='config',
            name='last_update_status',
            field=models.CharField(blank=True, choices=[('Pending', 'PENDING'), ('In Progress', 'IN_PROGRESS'), ('Error', 'ERROR'), ('Success', 'SUCCESS')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='schema',
            field=models.CharField(choices=[('http', 'http'), ('https', 'https')], default='http', max_length=5),
        ),
    ]
