# Generated by Django 4.1.4 on 2022-12-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a2zapp', '0002_alter_empmodel_dateofjoin'),
    ]

    operations = [
        migrations.CreateModel(
            name='calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=15)),
                ('Occation', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occation', models.CharField(max_length=1500)),
            ],
        ),
    ]
