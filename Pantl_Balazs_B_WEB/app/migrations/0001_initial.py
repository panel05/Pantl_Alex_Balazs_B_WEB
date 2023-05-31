# Generated by Django 4.2.1 on 2023-05-31 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('tema_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('temanev', models.CharField(max_length=50, verbose_name='temanev')),
            ],
        ),
        migrations.CreateModel(
            name='Szavak',
            fields=[
                ('szavak_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('angol', models.CharField(max_length=100, verbose_name='angol')),
                ('magyar', models.CharField(max_length=100, verbose_name='magyar')),
                ('temaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tema', verbose_name='temaId')),
            ],
        ),
    ]