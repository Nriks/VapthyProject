# Generated by Django 3.1 on 2020-08-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('creation_date', models.DateField()),
                ('creator', models.CharField(max_length=42)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'company',
            },
        ),
    ]
