# Generated by Django 4.2.3 on 2023-08-01 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_jobdetails_jobdescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetails',
            name='company_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
    ]
