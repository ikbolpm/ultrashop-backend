from django.db import models
import requests
from customers.models import Customer
from shop.models import Product
from stock.models import Inventory, Warehouse


class Order(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='order_warehouse')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_customer')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comments = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {} '.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return '{} '.format(self.id)

    @classmethod
    def telegram_bot_sendtext(cls, bot_message, bot_token, bot_chatID):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if not self.id:
            new_creation = True
        super().save(force_insert, force_update, using, update_fields)
        if new_creation:
            inventory, created = Inventory.objects.get_or_create(
                product=self.product,
                warehouse= self.order.warehouse,
                defaults= {'quantity': 0}
            )
            inventory.quantity = inventory.quantity - self.quantity
            inventory.save()
            message = 'Новая продажа! (Номер заказа: ' + str(self.order.id) +') \n\nПродукт: ' + str(
                self.product) + '\n\nКлиент: ' + self.order.customer.name + '\n\nМагазин: ' + self.order.warehouse.name + '\n\nКоличество: ' + str(
                self.quantity) + '\n\nЦена: $' + str(self.order.price) + '\n\nКомментарии: ' + self.order.comments
            bot_token = '876737347:AAGDgcS132vZemev47HC-8Evu8byJfHGoUg'
            bot_chatID = '-294089365'
            self.telegram_bot_sendtext(message, bot_token, bot_chatID)


class Inquiry(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    inquired_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inquired_product')
    STATUS_CHOICES = (
        ('NOT_CONTACTED', 'Not Contacted'),
        ('ATTEMPTED_TO_CONTACT', 'Attempted to Contact'),
        ('ASKED_TO_CALL_LATER', 'Asked to Call Later'),
        ('DECISION_MAKING', 'Decision Making'),
        ('CLOSED_WON', 'Closed Won'),
        ('CLOSED LOST', 'Closed Lost')
    )
    description = models.TextField(default='Empty')
    status = models.CharField(choices=STATUS_CHOICES, default='NOT_CONTACTED', max_length=50)
    sold_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sold_product', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if not self.id:
            new_creation = True
        super().save(force_insert, force_update, using, update_fields)
        message = 'Поступила новая заявка! Срочно позвоните! \n\nИмя: ' + self.name + '\n\nТелефон: '  + self.phone + '\n\nИнтересует: ' + str(self.inquired_product) + '\n\nМинимальная цена: $' + str(self.inquired_product.price)
        bot_token = '876737347:AAGDgcS132vZemev47HC-8Evu8byJfHGoUg'
        bot_chatID = '-294089365'
        if new_creation:
            OrderItem.telegram_bot_sendtext(message, bot_token, bot_chatID)