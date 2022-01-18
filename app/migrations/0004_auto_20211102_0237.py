# Generated by Django 3.2.8 on 2021-11-01 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='memo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]