from django.db import models
from django.utils import timezone

#My choices
ESTADO_CHOICES = (
	(u'acre', u'Acre'),
	(u'alagoas', u'Alagoas'),
	(u'amapá',u'Amapá'),
	(u'amazonas', u'Amazonas'),
	(u'bahia', u'Bahia'),
	(u'ceará', u'Ceará'),
	(u'distrito federal', u'Distrito Federal'),
	(u'espírito santo', u'Espírito Santo'),
	(u'goiás', u'Goiás'),
	(u'maranhão', u'Maranhão'),
	(u'mato grosso', u'Mato Grosso'),
	(u'mato grosso do sul', u'Mato Grosso do Sul'),
	(u'minas gerais', u'Minas Gerais'),
	(u'pará', u'Pará'),
	(u'paraíba', u'Paraíba'),
	(u'paraná', u'Paraná'),
	(u'pernambuco', u'Pernambuco'),
	(u'piauí', u'Piauí'),
	(u'rio de janeiro', u'Rio de Janeiro'),
	(u'rio grande do norte', u'Rio Grande do Norte'),
	(u'rio grande do sul', u'Rio Grande do Sul'),
	(u'rondônia', u'Rondônia'),
	(u'roraima', u'Roraima'),
	(u'santa catarina', u'Santa Catarina'),
	(u'são paulo', u'São Paulo'),
	(u'sergipe', u'Sergipe'),
	(u'tocantins', u'Tocantins'),
)

CATEGORIA_CHOICES = (
	(u'adaptador', u'Adaptador'),
	(u'desktop', u'Desktop'),
	(u'hardware', u'Hardware'),
	(u'impressora', u'Impressora'),
	(u'mouse', u'Mouse'),
	(u'notebook', u'Notebook'),
	(u'perifericos', u'Periféricos'),
	(u'smartphone', u'Smartphone'),
	(u'tablet', u'Tablet'),
	(u'teclado', u'Teclado'),
	(u'televisao', u'Televisão'),
)


# Create your models here.
class Produto(models.Model):
	id_produto = models.AutoField(primary_key=True)
	nome_produto = models.CharField(max_length=160)
	descricao_produto = models.TextField()
	imagem_produto = models.FileField(null=True, blank=True)
	categoria_produto = models.CharField(choices= CATEGORIA_CHOICES, max_length=200)
	preco_produto = models.DecimalField(max_digits=15, decimal_places=2)
	qntd_produto = models.IntegerField()	
	def __str__(self):
		return self.nome_produto


class Contato(models.Model):
	id_contato = models.AutoField(primary_key=True)
	contato_nome = models.CharField(max_length=200, unique=True)
	contato_email = models.EmailField(max_length=250)
	data_nascimento = models.DateField()
	telefone_de_contato = models.CharField(max_length=30)
	cpf_contato = models.IntegerField(unique=True)
	contato_estado = models.CharField(choices= ESTADO_CHOICES, max_length=200)
	contato_cidade = models.CharField(max_length=200)
	contato_endereco = models.CharField(max_length=400)
	def __str__(self):
		return self.contato_nome