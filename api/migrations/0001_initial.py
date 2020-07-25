# Generated by Django 3.0.8 on 2020-07-25 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
                ('start', models.DateTimeField(blank=True)),
                ('end', models.DateTimeField(blank=True)),
            ],
        ),
    ]
