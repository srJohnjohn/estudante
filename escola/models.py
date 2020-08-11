from django.db import models
from django.urls import reverse

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    nacimento = models.DateTimeField('data de nacimento')
    
    LOAN_STATUS = (
        ('r', 'Registrado'),
        ('m', 'Matriculado'),
        ('e', 'expulso'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='r',
        help_text='status do aluno',
    )

    def get_absolute_url(self):
        return  reverse('aluno_detail', args=[str(self.id)])

    def __str__(self):
        return self.nome
