# Generated by Django 3.0.3 on 2020-02-17 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_auto_20200217_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='STORE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_joinee', models.CharField(max_length=60)),
                ('device_assigned', models.CharField(max_length=60)),
                ('mouse_assigned', models.CharField(max_length=60)),
            ],
        ),
    ]
