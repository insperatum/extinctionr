# Generated by Django 2.2 on 2019-04-10 00:18

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PressRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(db_index=True)),
                ('released', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('body', markdownx.models.MarkdownxField(blank=True, default='')),
            ],
        ),
    ]