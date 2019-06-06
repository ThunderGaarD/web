# Generated by Django 2.1.7 on 2019-05-21 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'contato', 'verbose_name_plural': 'contatos'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='kind',
            field=models.CharField(choices=[('E', 'Email'), ('T', 'Telefone')], max_length=1, verbose_name='tipo'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Speaker', verbose_name='palestrante'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='value',
            field=models.CharField(max_length=255, verbose_name='valor'),
        ),
    ]
