# Generated by Django 4.1.4 on 2023-02-03 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=100)),
                ('admission_date', models.DateField()),
                ('admission_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('course', models.CharField(choices=[('BITAM', 'bitam'), ('BAGES', 'bages'), ('BSC', 'bcs')], max_length=25)),
                ('fathers_name', models.CharField(max_length=100)),
                ('fathers_number', models.IntegerField(unique=True)),
                ('mothers_name', models.CharField(max_length=100)),
                ('mothers_number', models.IntegerField()),
            ],
            options={
                'unique_together': {('admission_id', 'course')},
            },
        ),
    ]