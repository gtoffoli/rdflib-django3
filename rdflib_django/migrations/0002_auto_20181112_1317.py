# Generated by Django 2.1.3 on 2018-11-12 13:17

from django.db import migrations, models
import django.db.models.deletion
import rdflib_django.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rdflib_django', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namedgraph',
            name='identifier',
            field=rdflib_django.fields.URIField(db_index=True, max_length=500, verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='namespacemodel',
            name='prefix',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Prefix'),
        ),
        migrations.AlterField(
            model_name='namespacemodel',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rdflib_django.Store', verbose_name='Store'),
        ),
        migrations.AlterField(
            model_name='namespacemodel',
            name='uri',
            field=models.CharField(db_index=True, max_length=500, verbose_name='URI'),
        ),
        migrations.AlterField(
            model_name='store',
            name='identifier',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Identifier'),
        ),
        migrations.AlterUniqueTogether(
            name='namedgraph',
            unique_together={('identifier', 'store')},
        ),
        migrations.RemoveField(
            model_name='namespacemodel',
            name='fixed',
        ),
        migrations.AlterUniqueTogether(
            name='namespacemodel',
            unique_together={('prefix', 'store'), ('uri', 'store')},
        ),
    ]