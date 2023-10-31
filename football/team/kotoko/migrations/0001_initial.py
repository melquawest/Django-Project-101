# Generated by Django 4.2.5 on 2023-10-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('member_since', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
