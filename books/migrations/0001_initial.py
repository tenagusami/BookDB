# Generated by Django 2.0.5 on 2018-06-22 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_title', models.CharField(max_length=1000, unique=True)),
                ('volume', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=500)),
                ('publication_date', models.DateTimeField()),
                ('publisher', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('ISBN_13', models.CharField(max_length=30)),
                ('read', models.CharField(max_length=10)),
                ('storage', models.CharField(max_length=30)),
                ('book_info', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=50)),
                ('rental', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
