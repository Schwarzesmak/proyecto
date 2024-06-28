# Generated by Django 5.0.6 on 2024-06-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0010_alter_carrito_options_alter_carrito_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='usuario',
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='envio',
            name='estado',
            field=models.CharField(choices=[('ENTREGADO', 'Entregado'), ('CANCELADO', 'Cancelado'), ('PENDIENTE', 'Pendiente')], default='PENDIENTE', max_length=100),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('cancelado', 'Cancelado'), ('en_proceso', 'En Proceso'), ('finalizado', 'Finalizado')], default='en_proceso', max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='region',
            field=models.CharField(choices=[('ÑUBLE', 'Region del Ñuble'), ('BIOBIO', 'Region del Bio-Bio'), ('ARAUCANIA', 'Region de la Araucania')], default='CONCEPCION', max_length=25),
        ),
        migrations.AlterField(
            model_name='persona',
            name='region',
            field=models.CharField(choices=[('ÑUBLE', 'Region del Ñuble'), ('BIOBIO', 'Region del Bio-Bio'), ('ARAUCANIA', 'Region de la Araucania')], default='CONCEPCION', max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_municion',
            field=models.CharField(choices=[('POSTON', 'Poston'), ('AIRSOFT', 'Airsoft'), ('OTRO', 'Otro'), ('BALIN', 'Balin')], default='OTRO', max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(choices=[('ROPA', 'Ropa'), ('CUCHILLA', 'Cuchilla'), ('ARMA', 'Arma')], default='OTRO PRODUCTO', max_length=10),
        ),
    ]