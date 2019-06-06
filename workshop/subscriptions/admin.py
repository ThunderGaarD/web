from django.contrib import admin
from django.utils.timezone import now
from workshop.subscriptions.models import Subscriptions



class SubscriptionsAdmin(admin.ModelAdmin):

    list_display = ('name', 'cpf', 'email', 'phone', 'created_at', 'subscribed_today', 'paid')
    search_fields = ('name', 'cpf', 'email', 'phone')
    date_hierarchy = 'created_at'
    list_filter = ('paid', 'created_at',)

    actions = ['mark_as_paid']

    verbose_name = 'inscrição'
    verbose_name_plural = 'inscrições'


    def subscribed_today(self, obj):

        return obj.created_at.date() == now().date()


    subscribed_today.short_description = 'inscrito hoje?'

    subscribed_today.boolean = True


    def mark_as_paid(self, request, queryset):

        count = queryset.update(paid=True)

        if count == 1:
            msg = '{} Incrição Marcada como Paga'

        else:
            msg = '{} Inscrições Marcadas como Pagas'

        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar Selecionados como Pago'


admin.site.register(Subscriptions, SubscriptionsAdmin)
