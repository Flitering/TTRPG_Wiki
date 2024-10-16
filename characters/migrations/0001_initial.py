# Generated by Django 5.1.1 on 2024-09-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=50)),
                ('character_class', models.CharField(max_length=50)),
                ('level', models.IntegerField(default=1)),
                ('attributes', models.JSONField(default=dict)),
            ],
        ),
    ]
