# Generated by Django 4.2.7 on 2023-11-25 04:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projeto", "0002_rename_nota_avaliacao_notaapresentacao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="avaliacao",
            name="comentario",
            field=models.TextField(
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]
            ),
        ),
        migrations.AlterField(
            model_name="avaliacao",
            name="equipe",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to="projeto.equipe"),
        ),
        migrations.AlterField(
            model_name="avaliacao",
            name="notaApresentacao",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]
            ),
        ),
        migrations.AlterField(
            model_name="avaliacao",
            name="notaFuncionalidade",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]
            ),
        ),
    ]
