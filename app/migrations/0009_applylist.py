# Generated by Django 4.2.3 on 2023-08-02 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_jobdetails_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('min_salary', models.CharField(max_length=200)),
                ('max_salary', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('resume', models.FileField(upload_to='app/resume')),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jobdetails')),
            ],
        ),
    ]
