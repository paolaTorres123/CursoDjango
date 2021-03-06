# Generated by Django 3.1 on 2020-09-25 21:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grupo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Limpieza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salones', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='grupo.salones', verbose_name='Salones')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_personal', models.IntegerField(default=0, validators=[django.core.validators.MaxLengthValidator(9999, 'Error en la longitud'), django.core.validators.MinLengthValidator(1, 'Error de longitud mínima'), django.core.validators.RegexValidator('^[A-Za-zÀ-ÿ\\u00E0-\\u00FC ]+$', 'No se permiten caracteres especiales')], verbose_name='Total Personal:')),
                ('mujeres_personal', models.IntegerField(default=0, validators=[django.core.validators.MaxLengthValidator(999, 'Error en la longitud'), django.core.validators.MinLengthValidator(0, 'Error de longitud mínima'), django.core.validators.RegexValidator('^[A-Za-zÀ-ÿ\\u00E0-\\u00FC ]+$', 'No se permiten caracteres especiales')], verbose_name='Mujeres:')),
                ('hombres_personal', models.IntegerField(default=0, validators=[django.core.validators.MaxLengthValidator(999, 'Error en la longitud'), django.core.validators.MinLengthValidator(0, 'Error de longitud mínima'), django.core.validators.RegexValidator('^[A-Za-zÀ-ÿ\\u00E0-\\u00FC ]+$', 'No se permiten caracteres especiales')], verbose_name='Hombres:')),
                ('limpieza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='limpieza.limpieza', verbose_name='Limpieza')),
            ],
        ),
    ]
