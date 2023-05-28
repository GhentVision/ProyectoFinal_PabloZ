# Generated by Django 4.2.1 on 2023-05-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_estudios', '0004_curso_creador_estudiante_creador_profesor_creador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='descripcion',
            field=models.CharField(default='Descripción pendiente', max_length=60),
        ),
        migrations.AddField(
            model_name='curso',
            name='duracion',
            field=models.CharField(choices=[('1_mes', '1 mes'), ('2_meses', '2 meses'), ('3_meses', '3 meses'), ('4_meses', '4 meses')], default='1_mes', max_length=60),
        ),
    ]
