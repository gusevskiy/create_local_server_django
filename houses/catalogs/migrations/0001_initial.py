# Generated by Django 2.2.19 on 2023-03-23 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=300)),
                ('price', models.DecimalField(decimal_places=8, max_digits=8)),
            ],
        ),
    ]
