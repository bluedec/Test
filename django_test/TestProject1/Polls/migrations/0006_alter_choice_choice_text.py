# Generated by Django 4.1.3 on 2022-11-27 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0005_rename_question_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name='choice_text'),
        ),
    ]