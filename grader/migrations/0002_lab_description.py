# Generated by Django 2.1.4 on 2018-12-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='description',
            field=models.CharField(default='Default Description', max_length=4096),
            preserve_default=False,
        ),
    ]
