from django.db import models
from workshop.subscriptions.validators import validate_cpf
import uuid


class Subscriptions(models.Model):

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    name = models.CharField('nome', max_length=250)
    cpf = models.CharField('cpf', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField('pago', default=False)


    class Meta:

        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at',)


    def __str__(self):
        return self.name
