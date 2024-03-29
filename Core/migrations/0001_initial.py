# Generated by Django 2.1.7 on 2019-02-11 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projecte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(help_text='Nom del Projecte', max_length=200)),
                ('Descripcio', models.TextField(blank=True, default='Nou Projecte', null=True)),
                ('Grup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('Product_Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_Owner', to=settings.AUTH_USER_MODEL)),
                ('Scrum_Master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Scrum_Master', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Spec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcio', models.TextField()),
                ('Dificultad', models.CharField(choices=[('D', 'Desconeguda'), ('B', 'Baixa'), ('M', 'Mitjana'), ('A', 'Alta')], default='D', max_length=1)),
                ('Hores', models.IntegerField(default=0)),
                ('Developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Projecte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Projecte')),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_Inici', models.DateField()),
                ('Data_Final', models.DateField()),
                ('Hores', models.IntegerField(default=0, help_text='Hores Disponibles')),
                ('Projecte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Projecte')),
            ],
        ),
        migrations.AddField(
            model_name='spec',
            name='Sprint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Sprint'),
        ),
    ]
