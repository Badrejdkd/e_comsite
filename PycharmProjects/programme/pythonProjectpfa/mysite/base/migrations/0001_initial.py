# Generated by Django 5.2 on 2025-04-24 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('En cours', 'En cours'), ('Livrée', 'Livrée'), ('Annulée', 'Annulée')], default='En cours', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to='base.client')),
                ('compagnie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to='base.compagnie')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='produits/')),
                ('compagnie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produits', to='base.compagnie')),
            ],
        ),
    ]
