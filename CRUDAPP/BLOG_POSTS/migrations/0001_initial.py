# Generated by Django 3.1.7 on 2021-03-22 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_body', models.CharField(max_length=3000)),
                ('blog_author', models.CharField(max_length=200)),
            ],
        ),
    ]