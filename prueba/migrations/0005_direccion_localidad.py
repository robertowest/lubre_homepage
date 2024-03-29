# Generated by Django 2.2.5 on 2021-06-23 13:32

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0004_auto_20210513_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='localidad',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='departamento', chained_model_field='departamento', null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Localidad'),
        ),
    ]
