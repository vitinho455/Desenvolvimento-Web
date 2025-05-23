# Generated by Django 4.2.7 on 2023-11-03 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Processador', models.CharField(max_length=200)),
                ('MemoriaRam', models.CharField(max_length=200)),
                ('PlacaDeVideo', models.CharField(max_length=200)),
                ('FonteDeEnergia', models.CharField(max_length=200)),
                ('Gabinete', models.CharField(max_length=200)),
                ('Memoria', models.CharField(max_length=200)),
                ('Valor', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='PCs/')),
                ('Descricao', models.TextField(verbose_name='Descrição do Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Monitor', models.CharField(max_length=500)),
                ('Polegadas', models.CharField(max_length=30)),
                ('Megahertz', models.CharField(max_length=30)),
                ('Descricao', models.TextField(verbose_name='Descrição do Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Processador', models.CharField(max_length=200)),
                ('MemoriaRam', models.CharField(max_length=200)),
                ('PlacaDeVideo', models.CharField(max_length=200)),
                ('Memoria', models.CharField(max_length=200)),
                ('Descricao', models.TextField(verbose_name='Descrição do Produto')),
            ],
        ),
    ]
