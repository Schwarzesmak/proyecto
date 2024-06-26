# Generated by Django 5.0.6 on 2024-06-28 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_alter_envio_estado_alter_pedido_region_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.PROTECT, to='aplicacion.usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='region',
            field=models.CharField(choices=[('BIOBIO', 'Region del Bio-Bio'), ('ÑUBLE', 'Region del Ñuble'), ('ARAUCANIA', 'Region de la Araucania')], default='CONCEPCION', max_length=25),
        ),
        migrations.AlterField(
            model_name='persona',
            name='region',
            field=models.CharField(choices=[('BIOBIO', 'Region del Bio-Bio'), ('ÑUBLE', 'Region del Ñuble'), ('ARAUCANIA', 'Region de la Araucania')], default='CONCEPCION', max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(choices=[('CUCHILLA', 'Cuchilla'), ('ARMA', 'Arma'), ('ROPA', 'Ropa')], default='OTRO PRODUCTO', max_length=10),
        ),
    ]
