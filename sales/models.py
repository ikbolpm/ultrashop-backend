import requests
from django.db import models
from django.core.mail import send_mail

from accounts.models import User
from customers.models import Customer
from inventory.models import Inventory
from laptop.models import Laptop
from warehouses.models import Warehouse


class Sales(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, help_text='Выберите ноутбук')
    serial_number = models.CharField(max_length=255, help_text='Введите серийный номер')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, help_text='Выберите клиента')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, help_text='Выберите магазин/склад')
    price = models.DecimalField(max_digits=7, decimal_places=2, help_text='Цена за которую продали')
    quantity = models.IntegerField(help_text='Количество')
    profit = models.DecimalField(max_digits=7, decimal_places=2, help_text='Введите прибыль')
    comments = models.TextField(blank=True, null=True, help_text='Дополнительные комментарии, что в комплекте продали и т.д.')
    sold_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sales'
        verbose_name = 'Sale'

    def __str__(self):
        return self.laptop.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if not self.id:
            new_creation = True
        super().save(force_insert, force_update, using, update_fields)
        if new_creation:
            inventory, created = Inventory.objects.get_or_create(
                laptop=self.laptop,
                warehouse=self.warehouse,
                defaults={'quantity': 0}
            )
            inventory.quantity = inventory.quantity - self.quantity
            inventory.save()
            message = 'Продали ноутбук! \n\nНоутбук: ' + str(self.laptop) + '\n\nКлиент: ' + self.customer.name + '\n\nМагазин: ' + self.warehouse.name + '\n\nКоличество: ' + str(self.quantity) + '\n\nЦена: $' + str(self.price) + '\n\nПрибыль: $' + str(self.profit) + '\n\nКомментарии: ' + self.comments
            def telegram_bot_sendtext(bot_message):
                bot_token = '876737347:AAGDgcS132vZemev47HC-8Evu8byJfHGoUg'
                bot_chatID = '-257139211'
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


class CustomerReturns(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, help_text='Выберите ноутбук')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, help_text='Выберите магазин/склад')
    quantity = models.IntegerField(help_text='Количество')
    reason = models.TextField(help_text='Причина возврата')
    received_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Sales Returns'
        verbose_name = 'Sales Return'

    def __str__(self):
        return self.laptop.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        inventory, created = Inventory.objects.get_or_create(
            laptop=self.laptop,
            warehouse=self.warehouse,
            defaults={'quantity': 0}
        )
        inventory.quantity = self.quantity + inventory.quantity
        inventory.save()
        send_mail(
            'UltraShop.uz: Laptop Returned - ' + self.laptop.brand.name + ' ' + self.laptop.name + ' / ' + self.laptop.processor.name + ' / ' + str(
                self.laptop.ram) + ' / ' + str(self.laptop.main_storage),
            ' Laptop: ' + self.laptop.brand.name + ' ' + self.laptop.name + ' / ' + self.laptop.processor.name + ' / ' + str(
                self.laptop.ram) + ' / ' + str(
                self.laptop.main_storage) + '\n Warehouse: ' + self.warehouse.name + '\n Quantity: ' + str(
                self.quantity) + '\n Reason: ' + self.reason,
            'ultrashopsales@gmail.com',
            ['ikbolpm@gmail.com', 'mmamadjanov@gmail.com', 'mahkamov.farhodjon@gmail.com'],
            fail_silently=False,
        )