# Generated by Django 4.2.7 on 2023-11-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCs', '0002_monitor_valor_monitor_photo_notebook_valor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='Valor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='Valor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='Valor',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
