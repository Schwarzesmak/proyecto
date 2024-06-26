# Generated by Django 5.0.6 on 2024-06-26 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0009_alter_carrito_envio_alter_pedido_region_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrito',
            options={'verbose_name_plural': 'Carritos'},
        ),
        migrations.AlterField(
            model_name='carrito',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carritos', to='aplicacion.usuario'),
        ),
        migrations.AlterField(
            model_name='envio',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('ENTREGADO', 'Entregado'), ('CANCELADO', 'Cancelado')], default='PENDIENTE', max_length=100),
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
            name='tipo_municion',
            field=models.CharField(choices=[('BALIN', 'Balin'), ('OTRO', 'Otro'), ('POSTON', 'Poston'), ('AIRSOFT', 'Airsoft')], default='OTRO', max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(choices=[('CUCHILLA', 'Cuchilla'), ('ARMA', 'Arma'), ('ROPA', 'Ropa')], default='OTRO PRODUCTO', max_length=10),
        ),
    ]
