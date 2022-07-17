# Generated by Django 4.0.6 on 2022-07-17 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desciption', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='porfolio/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]