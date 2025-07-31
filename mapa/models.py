from django.db import models

class Ilha(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.ImageField(upload_to='icones_ilhas/')

    def __str__(self):
        return self.nome

CATEGORIAS = [
    ('boss', 'Boss'),
    ('bau', 'Baú'),
    ('mob', 'Mob'),
    ('quest', 'Quest'),
    ('achievement', 'Achievement'),
]

class Informacao(models.Model):
    ilha = models.ForeignKey(Ilha, on_delete=models.CASCADE, related_name='localizacoes')
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    imagem = models.ImageField(upload_to='localizacoes/')
    ponto_referencia = models.TextField(blank=True, null=True)
    recompensa = models.CharField(max_length=200, blank=True, null=True)  # novo campo

    def __str__(self):
        return f"{self.get_categoria_display()} em {self.ilha.nome}"
