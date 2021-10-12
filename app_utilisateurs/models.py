from django.db import models

class Utilisateur(models.Model):
    CIVIL = (
        ('Mr', 'Monsieur'),
        ('Mme', 'Madame'),
        ('Mlle', 'Mademoiselle')
    )

    util_civil = models.CharField(verbose_name='Civilité', max_length=4, choices=CIVIL)
    util_first_name = models.CharField(verbose_name='Prénom', max_length=50, null=True, blank=True, )
    util_last_name = models.CharField(verbose_name='Nom', max_length=50)
    util_email = models.EmailField(verbose_name="Email @", max_length=254, unique=True)
    util_phone1 = models.CharField(verbose_name="N° Téléphone", blank=True, null=True, max_length=15)

    class Meta:
        verbose_name_plural = "Utilisateurs"
        constraints = [models.UniqueConstraint(fields=['util_first_name', 'util_last_name'], name="unique_utilisateur")]
        indexes = [models.Index(fields=['util_last_name'], name='I_Utilisateur')]