# Generated by Django 4.0.5 on 2022-06-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_producto_id_producto_alter_producto_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Nombre Del Producto'),
        ),
    ]
