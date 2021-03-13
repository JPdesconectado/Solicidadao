from django.db import models
from requests.models import Endereco 
from cpf_field.models import CPFField


class EnviarEmailTransito(models.Model):
    email = models.EmailField(max_length=254)
    tipo =  models.CharField(max_length = 50)
    endereco = models.ForeignKey(Endereco, on_delete = models.CASCADE)
    imagem = models.ImageField(upload_to = 'imagens/', blank=True)

class EnviarEmailEducacao(models.Model):
    email = models.EmailField(max_length=254)
    cadastro_pf = CPFField('CPF')
    rg = models.CharField(max_length = 15)    

class EnviarEmailIluminacao(models.Model):
    email = models.EmailField(max_length=254)
    rg = models.CharField(max_length = 15)
    conta_luz = models.FileField(upload_to = 'arquivos/')

class EnviarEmailMeioAmbiente(models.Model):
    email = models.EmailField(max_length=254)
    endereco = models.ForeignKey(Endereco, on_delete = models.CASCADE)