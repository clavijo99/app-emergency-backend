# Generated by Django 4.0.4 on 2024-02-03 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Emergency',
                'verbose_name_plural': 'Emergencies',
            },
        ),
    ]
