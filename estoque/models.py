from django.db import models

class Peca(models.Model):
    TAMANHOS = [
    ('PP', 'PP'), ('P', 'P'), ('M', 'M'),
    ('G', 'G'), ('GG', 'GG'), ('XGG', 'XGG'),
    ('34', '34'), ('36', '36'), ('38', '38'),
    ('40', '40'), ('42', '42'), ('44', '44'),
    ('46', '46'), ('48', '48'), ('50', '50'),
]

    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True, null=True)
    tamanho = models.CharField(max_length=5, choices=TAMANHOS, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    valor_diaria = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.codigo} — {self.nome}'

    class Meta:
        ordering = ['nome']
        verbose_name = 'Peça'
        verbose_name_plural = 'Peças'