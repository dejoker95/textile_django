# Generated by Django 3.1.3 on 2020-11-23 12:05

from django.db import migrations, models
import frontpage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to=frontpage.models.user_path)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
