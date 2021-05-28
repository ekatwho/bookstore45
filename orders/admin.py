from django.contrib import admin
from .models import Delivery, Payment, Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe


import csv
import datetime
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' \
                                      'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many \
              and not field.one_to_many]
    # Записываем первую строку с заголовками полей.
    writer.writerow([field.verbose_name for field in fields])
    # Записываем данные.
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'


def order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id])))


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['d_type', 'd_price']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['p_type']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'city',
                    'address',
                    'paid',
                    'ord_check_time']
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline]
    actions = [export_to_csv]


