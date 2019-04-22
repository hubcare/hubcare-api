# Generated by Django 2.1.7 on 2019-04-21 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commits', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None)),
                ('quantity', models.IntegerField()),
                ('commit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commits.Commit')),
            ],
        ),
    ]
