# Generated by Django 3.1.5 on 2023-01-14 21:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id_code', models.CharField(auto_created=True, default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False, verbose_name='mail')),
                ('name', models.CharField(default='Untitled', max_length=128)),
                ('content', models.CharField(default='Under Review', max_length=128)),
                ('unread', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
