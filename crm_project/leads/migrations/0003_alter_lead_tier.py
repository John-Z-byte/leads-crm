# Generated by Django 5.1.6 on 2025-02-25 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_rename_type_lead_lead_type_alter_lead_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='tier',
            field=models.CharField(choices=[('0-75 $', '0-75 $'), ('76-199 $', '76-199 $'), ('200-329 $', '200-329 $')], max_length=10),
        ),
    ]
