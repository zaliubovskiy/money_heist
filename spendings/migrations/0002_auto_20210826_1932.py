# Generated by Django 3.2.6 on 2021-08-26 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spendings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spendings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='spendingcategory',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]