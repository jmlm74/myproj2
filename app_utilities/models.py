from django.db import models
from django.db.models import UniqueConstraint


class PieceJointe(models.Model):

    pj_ident = models.CharField(max_length=50, verbose_name='Identification')
    pj_fichier = models.FileField(upload_to='pj/', max_length=100, verbose_name='Pièce jointe',
                                  default="")

    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Pièce jointe"
        verbose_name_plural = "Pièces jointes"
        constraints = [UniqueConstraint(fields=['pj_ident'], name="Unique_pj_ident"),
                       UniqueConstraint(fields=['pj_fichier'], name="Unique_pj_fichier")]
        indexes = [models.Index(fields=['pj_ident'], name='I_pj_ident'),
                   ]

    def __str__(self):
        return self.pj_identification
