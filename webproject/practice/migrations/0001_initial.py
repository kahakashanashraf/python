# Generated by Django 3.0.7 on 2021-02-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myprc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='prcimage/')),
                ('Title', models.CharField(max_length=50)),
                ('Desc', models.TextField(blank=True, max_length=500)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
