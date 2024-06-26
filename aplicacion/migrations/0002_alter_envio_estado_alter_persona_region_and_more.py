# Generated by Django 5.0.6 on 2024-06-14 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='estado',
            field=models.CharField(choices=[('ENTREGADO', 'Entregado'), ('PENDIENTE', 'Pendiente'), ('CANCELADO', 'Cancelado')], default='ENTREGADO', max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='region',
            field=models.CharField(choices=[('ARAUCANIA', 'Region de la Araucania'), ('BIOBIO', 'Region del Bio-Bio'), ('ÑUBLE', 'Region del Ñuble')], default='CONCEPCION', max_length=25),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo_municion',
            field=models.CharField(choices=[('BALIN', 'Balin'), ('AIRSOFT', 'Airsoft'), ('OTRO', 'Otro'), ('POSTON', 'Poston')], default='OTRO', max_length=100),
        ),
    ]
