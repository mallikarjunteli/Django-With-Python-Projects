# Generated by Django 4.1.3 on 2022-11-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=50)),
                ('disease', models.CharField(max_length=50)),
            ],
        ),
    ]