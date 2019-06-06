from django.db import models


class Speaker(models.Model):

    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    website = models.URLField('website', blank=True)
    photo = models.URLField('foto')
    description = models.TextField('descrição', blank=True)
    skill = models.CharField('habilidade', max_length=100, blank=True)


    class Meta:

        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'


    def __str__(self):

        return self.name


class Contact(models.Model):

    EMAIL = 'E'
    TELEFONE = 'T'

    KINDS = ((EMAIL, 'Email'),
             (TELEFONE, 'Telefone'),)

    speaker = models.ForeignKey('Speaker', on_delete=models.CASCADE,
                                verbose_name='palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)


    class Meta:

        verbose_name = 'contato'
        verbose_name_plural = 'contatos'


    def __str__(self):

        return self.value


class Talk(models.Model):

    title = models.CharField('título', max_length=200)
    local = models.CharField('local', max_length=100, blank=True)
    date = models.DateField('data')
    start = models.TimeField('início', blank=True, null=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField('Speaker',
                                      verbose_name='palestrantes',
                                      blank=True)


    class Meta:

        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'


    def __str__(self):

        return self.title