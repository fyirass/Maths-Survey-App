# Generated by Django 4.0.4 on 2022-06-24 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_alter_question_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='mathsurveyapp@gmail.com', max_length=200, verbose_name='email')),
                ('comment', models.CharField(max_length=200, verbose_name='comment')),
            ],
        ),
    ]
