# Generated by Django 5.0.6 on 2024-06-16 23:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_pedido_registro_alter_persona_correo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='estado',
            field=models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('CANCELADO', 'Cancelado'), ('ENTREGADO', 'Entregado')], default='ENTREGADO', max_length=100),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='boleta',
            field=models.CharField(choices=[('sin_boleta', 'Sin boleta'), ('con_boleta', 'Con boleta')], max_length=15),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='region',
            field=models.CharField(choices=[('ÑUBLE', 'Region del Ñuble'), ('ARAUCANIA', 'Region de la Araucania'), ('BIOBIO', 'Region del Bio-Bio')], default='CONCEPCION', max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_municion',
            field=models.CharField(choices=[('AIRSOFT', 'Airsoft'), ('OTRO', 'Otro'), ('POSTON', 'Poston'), ('BALIN', 'Balin')], default='OTRO', max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_producto',
            field=models.CharField(choices=[('CUCHILLA', 'Cuchilla'), ('ROPA', 'Ropa'), ('ARMA', 'Arma')], default='OTRO PRODUCTO', max_length=10),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('usuario', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('envio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='aplicacion.envio')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.producto')),
            ],
        ),
    ]
