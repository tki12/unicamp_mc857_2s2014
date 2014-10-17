from django.db import models



# Create your models here.

# Table containing the data for every single trip
# The fields related to geographic info must be
# adapted to reflect the format used bt the service.
class Route(models.Model):
    traveller = models.ForeignKey(UserData)
    source = models.CharField(max_length=100, help_text=u"Ponto de Origem")
    dest = models.CharField(max_length=100, help_text=u"Ponto de Destino")
    sourceTime = models.DateTimeField(help_text=u"Data de Partida")
    destTime = models.DateTimeField(help_text=u"Data de Chegada")
    addTime  = models.DateTimeField(auto_now_add=True, help_text=u"Data de Criação da Viagem")
	pass

# Table for user data
# New fields must be added, but those are the bare essentials
class UserData(models.Model):
    username = models.CharField("Login", max_length=30, primary_key=True, unique=True)
    email = models.CharField(max_length=30, unique=True)
    realname = models.CharField("Nome Verdadeiro", max_length=200, help_text=u"Nome real do usuário")
    cpf = models.CharField(max_length=12, help_text=u"CPF (números apenas)")
	pass

# Table for storing users' reviews of one another
# Each review must be associated with a trip involving both parts
class UserReview(models.Model):
    GRADES = (
        ('G', 'Positiva'),
        ('B', 'Negativa')
        )
    reviewer = models.ForeignKey(UserData, verbose_name=u"Usuário Avaliado")
    reviewed = models.ForeignKey(UserData, verbose_name=u"Usuário Avaliador")
    trip = models.ForeignKey(Route, verbose_name=u"Viagem Avaliada")
    grade = models.CharField(u"Avaliação da Transação", max_length=1, choices=GRADES, help_text=u"Avaliação do usuário sobre a transação.")
    comment = models.CharField(u"Comentários", max_length=1000, blank=True, help_text=u"Comentários sobre a avaliação")
	pass
