# Generated by Django 2.2.4 on 2021-05-13 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_auto_20210513_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Departamento'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='localidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Localidad'),
        ),
    ]
