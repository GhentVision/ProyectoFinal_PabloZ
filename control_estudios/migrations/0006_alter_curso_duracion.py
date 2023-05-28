# Generated by Django 4.2.1 on 2023-05-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_estudios', '0005_post_curso_descripcion_curso_duracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='duracion',
            field=models.CharField(choices=[('1 mes', '1 mes'), ('2 meses', '2 meses'), ('3 meses', '3 meses'), ('4 meses', '4 meses')], default='1_mes', max_length=60),
        ),
    ]
