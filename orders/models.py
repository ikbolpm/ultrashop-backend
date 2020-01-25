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

            # message = 'Продали ноутбук! \n\nНоутбук: ' + str(self.laptop) + '\n\nКлиент: ' + self.customer.name + '\n\nМагазин: ' + self.warehouse.name + '\n\nКоличество: ' + str(self.quantity) + '\n\nЦена: $' + str(self.price) + '\n\nПрибыль: $' + str(self.profit) + '\n\nКомментарии: ' + self.comments
            def telegram_bot_sendtext(bot_message):
                bot_token = '876737347:AAGDgcS132vZemev47HC-8Evu8byJfHGoUg'
                bot_chatID = '-294089365'
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

                response = requests.get(send_text)
                return response.json()

            telegram_bot_sendtext(message)
            # send_mail(
            #     'UltraShop.uz: New Laptop Sold - ' + self.laptop.brand.name + ' ' + self.laptop.name + ' / ' + self.laptop.processor.name + ' / ' + str(self.laptop.ram) + ' / ' + str(self.laptop.main_storage),
            #     ' Laptop: ' + self.laptop.brand.name + ' ' + self.laptop.name + ' / ' + self.laptop.processor.name + ' / ' + str(self.laptop.ram) + ' / ' + str(self.laptop.main_storage) + '\n Customer: ' + self.customer.name + '\n Warehouse: ' + self.warehouse.name + '\n Quantity: ' + str(self.quantity) + '\n Price: $' + str(self.price) + '\n Profit: $' + str(self.profit) + '\n Comments: ' + self.comments,
            #     'ultrashopsales@gmail.com',
            #     ['ikbolpm@gmail.com', 'mmamadjanov@gmail.com', 'mahkamov.farhodjon@gmail.com'],
            #     fail_silently=False,
            # )