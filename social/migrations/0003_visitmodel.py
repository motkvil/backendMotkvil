# Generated by Django 4.1.4 on 2023-03-08 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_newsmodel_viewsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
