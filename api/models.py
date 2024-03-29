from django.db.models.signals import post_save
from django.db import models

# Create your models here.


class Raid(models.Model):
    NAMES = (
        ('onyxia', 'onyxia'),
        ('mc', 'molten core')
    )

    name = models.CharField(
        choices=NAMES, verbose_name="Nombre", max_length=150)
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
        ('oficial', 'oficial'),
        ('raid', 'raid'),
        ('trial', 'trial'),
        ('member', 'member'),
        ('kicked', 'kicked')
    )

    ROLES = (
        ('tank', 'tank'),
        ('dps', 'dps'),
        ('healer', 'healer'),
        ('hybrid', 'hybrid')
    )

    CLASES = (
        ('warlock', 'Brujo'),
        ('hunter', 'Cazador'),
        ('druid', 'Druida'),
        ('warrior', 'Guerrero'),
        ('mage', 'Mago'),
        ('rogue', 'Picaro'),
        ('priest', 'Sacerdote')
    )

    name = models.CharField(
        max_length=90, verbose_name="Nickname", unique=True)
    rank = models.CharField(choices=TYPE, verbose_name="Rango", max_length=150)
    role = models.CharField(choices=ROLES, verbose_name="Rol", max_length=150)
    clas = models.CharField(
        choices=CLASES, verbose_name="Clase", max_length=150)
    joined = models.DateField(blank=True, null=True,
                              verbose_name="Fecha de entrada")
    notes = models.TextField(blank=True, null=True, verbose_name="Notas")

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ['name']

    def __str__(self):
        return self.name


class RaidAssistance(models.Model):
    member = models.ForeignKey(
        Member, verbose_name="Miembro", on_delete=models.CASCADE)
    raid = models.ForeignKey(Raid, verbose_name="Raid",
                             on_delete=models.CASCADE, related_name='raid_assistances')
    assistance = models.BooleanField(default=False, verbose_name="Asistencia")

    class Meta:
        verbose_name = "Assistance"
        verbose_name_plural = "Assistances"
        unique_together = ['member', 'raid']

    def __str__(self):
        return self.member.name


def create_raid_assistance(sender, instance, created, **kwargs):
    if created:
        members = Member.objects.all()

        for member in members:
            raid_assistance = RaidAssistance()
            if member.rank != 'member' and member.rank != 'kicked':
                raid_assistance.member = member
            raid_assistance.raid = instance
            raid_assistance.save()


post_save.connect(create_raid_assistance, sender=Raid)
