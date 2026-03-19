from django.db import models
from clientes.models import Cliente
from estoque.models import Peca

class Reserva(models.Model):
    STATUS = [
        ('reservado', 'Reservado'),
        ('retirado', 'Retirado'),
        ('devolvido', 'Devolvido'),
        ('atrasado', 'Atrasado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='reservas')
    peca = models.ForeignKey(Peca, on_delete=models.PROTECT, related_name='reservas')
    status = models.CharField(max_length=20, choices=STATUS, default='reservado')
    data_retirada = models.DateField()
    data_devolucao = models.DateField()
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Se status indica que a peça está em uso, marca como indisponível
        if self.status in ['reservado', 'retirado', 'atrasado']:
            self.peca.disponivel = False
        # Se foi devolvida ou cancelada, libera a peça
        elif self.status in ['devolvido', 'cancelado']:
            self.peca.disponivel = True
        self.peca.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.cliente.nome} — {self.peca.nome} ({self.status})'

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'