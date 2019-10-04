# Generated by Django 2.2.6 on 2019-10-03 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, unique=True, verbose_name='Nickname')),
                ('rank', models.CharField(choices=[('raid', 'raid'), ('trial', 'trial'), ('member', 'member'), ('kicked', 'kicked')], max_length=150, verbose_name='Rango')),
                ('role', models.CharField(choices=[('tank', 'tank'), ('dps', 'dps'), ('healer', 'healer'), ('hybrid', 'hybrid')], max_length=150, verbose_name='Rol')),
                ('clas', models.CharField(choices=[('warlock', 'Brujo'), ('hunter', 'Cazador'), ('druid', 'Druida'), ('warrior', 'Guerrero'), ('mage', 'Mago'), ('rogue', 'Picaro'), ('priest', 'Sacerdote')], max_length=150, verbose_name='Clase')),
                ('joined', models.DateField(blank=True, null=True, verbose_name='Fecha de entrada')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notas')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Raid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('onyxia', 'onyxia'), ('mc', 'molten core')], max_length=150, verbose_name='Nombre')),
                ('day', models.DateField(verbose_name='Dia del evento')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notas')),
            ],
            options={
                'verbose_name': 'Raid',
                'verbose_name_plural': 'Raids',
                'ordering': ['-day'],
            },
        ),
        migrations.CreateModel(
            name='RaidAssistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistance', models.BooleanField(default=False, verbose_name='Asistencia')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Member', verbose_name='Miembro')),
                ('raid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raid_assistances', to='api.Raid', verbose_name='Raid')),
            ],
            options={
                'verbose_name': 'Assistance',
                'verbose_name_plural': 'Assistances',
                'unique_together': {('member', 'raid')},
            },
        ),
    ]