from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

# Create your models here.

class Projecte(models.Model):
	Nom	=	models.CharField(
			max_length	=	200,
			help_text	=	"Nom del Projecte"
			)
	Descripcio	=	models.TextField(
					blank	=	True,
					null	=	True,
					default	=	"Nou Projecte"
					)
	Scrum_Master	=	models.ForeignKey(
        				settings.AUTH_USER_MODEL,
        				on_delete = models.CASCADE,
        				related_name	=	"Scrum_Master",
        				)
	Product_Owner	=	models.ForeignKey(
        				settings.AUTH_USER_MODEL,
        				on_delete = models.CASCADE,
        				related_name	=	"Product_Owner",
        				)
	Grup 	=	models.ForeignKey(
				Group,
				on_delete = models.CASCADE,
				)
	def __str__(self):
		return self.Nom

class Sprint(models.Model):
	Projecte	=	models.ForeignKey(
					Projecte,
					on_delete = models.CASCADE
					)
	Data_Inici	=	models.DateField()
	Data_Final	=	models.DateField()
	Hores	=	models.IntegerField(
				default = 0,
				help_text = "Hores Disponibles"
				)
	def __str__(self):
		return self.Projecte.Nom

class Spec(models.Model):
	Dificult 	=	(
					("D","Desconeguda"),
					("B","Baixa"),
					("M","Mitjana"),
					("A","Alta")
					)
	Descripcio	=	models.TextField()
	Dificultad	=	models.CharField(
					max_length = 1,
					choices = Dificult,
					default = "D"
					)
	Hores	=	models.IntegerField(
				default = 0
				)
	Projecte	=	models.ForeignKey(
					Projecte,
					on_delete	=	models.CASCADE,
					)
	Sprint	=	models.ForeignKey(
				Sprint,
				on_delete	=	models.CASCADE,
				)
	Developer	=	models.ForeignKey(
					settings.AUTH_USER_MODEL,
					on_delete	=	models.CASCADE,
					)
	def __str__(self):
		return self.Descripcio