# Generated by Django 4.2.2 on 2023-07-11 21:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plantitas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.BigIntegerField()),
                ('fechaCompra', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='cantidad',
            field=models.IntegerField(blank=True, verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='precio',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
        migrations.CreateModel(
            name='detalle_boleta',
            fields=[
                ('id_detalle_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.BigIntegerField()),
                ('id_boleta', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='plantitas.boleta')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plantitas.stock')),
            ],
        ),
    ]
