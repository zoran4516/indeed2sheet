# Generated by Django 3.0.5 on 2020-04-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200407_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(default='https://www.indeed.com/jobs?q=%22Proofreader%22+OR+%22Editor%22&sort=date', max_length=255)),
            ],
        ),
    ]
