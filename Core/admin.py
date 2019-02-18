from django.contrib import admin
from Core.models import *

# Register your models here.

class InlineSpec(admin.TabularInline):
	model =	Spec
	extra = 0

class InlineSprint(admin.TabularInline):
	model =	Sprint
	extra = 1

class ProjecteAdmin(admin.ModelAdmin):
	inlines =	[InlineSprint,InlineSpec]	

class SprintAdmin(admin.ModelAdmin):
	list_display	=	['Projecte','Data_Inici','Data_Final','Hores']

class SpecAdmin(admin.ModelAdmin):
	list_display	=	['Descripcio','Dificultad','Hores','Projecte','Sprint','Developer']

admin.site.register(Projecte,ProjecteAdmin)
admin.site.register(Spec,SpecAdmin)
admin.site.register(Sprint,SprintAdmin)