# Generated by Django 5.1.1 on 2024-09-14 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_establecimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id_etiqueta', models.AutoField(primary_key=True, serialize=False)),
                ('texto_etiqueta', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='establecimiento',
            name='tipo_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipoestablecimiento'),
        ),
    ]