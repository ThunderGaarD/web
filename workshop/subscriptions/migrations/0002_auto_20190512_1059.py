# Generated by Django 2.1.7 on 2019-05-12 10:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriptions',
            options={'ordering': ('-created_at',), 'verbose_name': 'inscrição', 'verbose_name_plural': 'inscrições'},
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='pago'),
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='name',
            field=models.CharField(max_length=250, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='telefone'),
        ),
    ]