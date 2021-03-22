# Generated by Django 3.1.7 on 2021-03-20 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_user', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_text', models.CharField(max_length=200)),
            ],
        ),
    ]
