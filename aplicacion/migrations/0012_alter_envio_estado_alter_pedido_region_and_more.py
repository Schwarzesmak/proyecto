# Generated by Django 5.0.6 on 2024-06-28 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0011_remove_pedido_productos_remove_pedido_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('ENTREGADO', 'Entregado'), ('CANCELADO', 'Cancelado')], default='PENDIENTE', max_length=100),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='region',
            field=models.CharField(choices=[('BIOBIO', 'Region del Bio-Bio'), ('ARAUCANIA', 'Region de la Araucania'), ('ÑUBLE', 'Region del Ñuble')], default='CONCEPCION', max_length=25),
        ),
        migrations.AlterField(
            model_name='persona',
            name='region',
            field=models.CharField(choices=[('BIOBIO', 'Region del Bio-Bio'), ('ARAUCANIA', 'Region de la Araucania'), ('ÑUBLE', 'Region del Ñuble')], default='CONCEPCION', max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_municion',
            field=models.CharField(choices=[('AIRSOFT', 'Airsoft'), ('BALIN', 'Balin'), ('POSTON', 'Poston'), ('OTRO', 'Otro')], default='OTRO', max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(choices=[('ARMA', 'Arma'), ('CUCHILLA', 'Cuchilla'), ('ROPA', 'Ropa')], default='OTRO PRODUCTO', max_length=10),
        ),
    ]
