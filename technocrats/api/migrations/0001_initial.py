# Generated by Django 2.1.3 on 2018-11-22 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucketlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bucketlists', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'techno_bucketlist',
            },
        ),
    ]
