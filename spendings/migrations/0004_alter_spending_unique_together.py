# Generated by Django 3.2.6 on 2021-08-27 08:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spendings', '0003_alter_spending_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spending',
            unique_together={('user', 'category')},
        ),
    ]