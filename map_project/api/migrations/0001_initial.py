# Generated by Django 4.1.3 on 2022-11-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(default='100 Green St.', max_length=50, unique='False')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
