from django.db import models

# Create your models here.
class Raid(models.Model):
    NAMES = (
        ('onyxia': 'onyxia'),
        ('mc': 'molten core')
    )

    name = models.CharField(choices=NAMES, verbose_name="Nombre")
    day = models.DateField(verbose_name="Dia del evento")
    notes = models.TextField(blank=True, null=True, verbose_name="Notas")

    class Meta:
        verbose_name = "Raid"
        verbose_name_plural = "Raids"
        ordering = ['-day']

    def __str__(self):
       return self.name


class Member(models.Model):
    TYPE = (
        ('raid': 'raid'),
        ('trial': 'trial'),
        ('member': 'member'),
        ('kicked': 'kicked')
    )

    ROLES = (
        ('tank': 'tank'),
        ('dps': 'dps'),
        ('healer': 'healer'),
        ('hybrid': 'hybrid')
    )

    CLASES = (
        ('warlock': 'Brujo'),
        ('hunter': 'Cazador'),
        ('druid': 'Druida'),
        ('warrior': 'Guerrero'),
        ('mage': 'Mago'),
        ('rogue': 'Picaro'),
        ('priest': 'Sacerdote')
    )

    name = models.CharField(max_length=90, verbose_name="Nickname", unique=True)
    rank = models.CharField(choices=TYPE, verbose_name="Rango")
    role = models.CharField(choices=ROLES, verbose_name="Rol")
    clas = models.CharField(choices=CLASES, verbose_name="Clase")
    joined = models.DateField(blank=True, null=True, verbose_name="Fecha de entrada")
    notes = models.TextField(blank=True, null=True, verbose_name="Notas")

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ['name']

    def __str__(self):
        return self.name


class RaidAssistance(models.Model):
    member = models.ForeignKey(Member, verbose_name="Miembro", on_delete=models.CASCADE)
    raid = models.ForeignKey(Raid, verbose_name="Raid", on_delete=models.CASCADE)
    assistance = models.BooleanField(default=False, verbose_name="Asistencia")

    class Meta:
        verbose_name = "Assistance"
        verbose_name_plural = "Assistances"
        unique_together = ['member', 'raid']
