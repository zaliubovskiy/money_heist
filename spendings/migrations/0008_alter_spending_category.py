# Generated by Django 3.2.6 on 2021-08-28 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spendings', '0007_auto_20210827_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='spendings', to='spendings.spendingcategory'),
        ),
    ]
