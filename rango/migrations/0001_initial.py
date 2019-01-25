# Generated by Django 2.1.5 on 2019-01-11 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=126)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Category')),
            ],
        ),
    ]