# Generated by Django 5.0.6 on 2024-06-25 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_alter_carrito_usuario_alter_pedido_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='estado',
            field=models.CharField(choices=[('ENTREGADO', 'Entregado'), ('PENDIENTE', 'Pendiente'), ('CANCELADO', 'Cancelado')], default='PENDIENTE', max_length=100),
        ),
        migrations.AlterField(
            model_name='envio',
            name='fecha_compra',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de compra'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_municion',
            field=models.CharField(choices=[('POSTON', 'Poston'), ('BALIN', 'Balin'), ('OTRO', 'Otro'), ('AIRSOFT', 'Airsoft')], default='OTRO', max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(choices=[('CUCHILLA', 'Cuchilla'), ('ROPA', 'Ropa'), ('ARMA', 'Arma')], default='OTRO PRODUCTO', max_length=10),
        ),
    ]
