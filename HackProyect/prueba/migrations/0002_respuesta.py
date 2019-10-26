# Generated by Django 2.2.6 on 2019-10-26 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.Pregunta')),
            ],
        ),
    ]
