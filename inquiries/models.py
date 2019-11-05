import requests

from django.db import models
from django.core.mail import send_mail
from resolution.models import Resolution
from ram.models import Ram
from processorBrand.models import ProcessorBrand
from laptopType.models import LaptopType
from displaySize.models import DisplaySize
from settings.models import DollarExchangeRate, TransactionCoefficient
from storage.models import Storage
from laptop.models import Laptop
from products.models import Product

class Inquiry(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    # comments = models.TextField(blank=True, null=True)
    # size = models.ManyToManyField(DisplaySize, blank=True)
    # ram = models.ManyToManyField(Ram, blank=True)
    laptop = models.ForeignKey(Laptop, blank=True, null=True, on_delete=models.CASCADE, related_name='inquired_laptop')
    # resolution = models.ManyToManyField(Resolution, blank=True)
    # storage = models.ManyToManyField(Storage, blank=True)
    # type = models.ManyToManyField(LaptopType, blank=True)
    # source = models.CharField(max_length=200)
    # processor = models.ManyToManyField(ProcessorBrand, blank=True)
    # min_price = models.CharField(max_length=50, blank=True, null=True)
    # max_price = models.CharField(max_length=50, blank=True, null=True)
    # min_cores = models.CharField(max_length=50, blank=True, null=True)
    # max_cores = models.CharField(max_length=50, blank=True, null=True)
    # min_size = models.CharField(max_length=4, blank=True, null=True)
    # max_size = models.CharField(max_length=4, blank=True, null=True)
    # min_storage = models.CharField(max_length=50, blank=True, null=True)
    # max_storage = models.CharField(max_length=50, blank=True, null=True)
    # min_ram = models.CharField(max_length=50, blank=True, null=True)
    # max_ram = models.CharField(max_length=50, blank=True, null=True)
    STATUS_CHOICES = (
        ('NOT_CONTACTED', 'Not Contacted'),
        ('ATTEMPTED_TO_CONTACT', 'Attempted to Contact'),
        ('ASKED_TO_CALL_LATER', 'Asked to Call Later'),
        ('DECISION_MAKING', 'Decision Making'),
        ('CLOSED_WON', 'Closed Won'),
        ('CLOSED LOST', 'Closed Lost')
    )
    description = models.TextField(default='Empty')
    status = models.CharField(choices=STATUS_CHOICES, default='NOT_CONTACTED', max_length=30)
    # sold = models.ForeignKey(Laptop, blank=True, null=True, on_delete=models.CASCADE, related_name='sold_laptop')

    class Meta:
        verbose_name_plural = 'Inquiries'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if not self.id:
            new_creation = True
        super().save(force_insert, force_update, using, update_fields)
        message = 'Поступила новая заявка! Срочно позвоните! \n\nИмя: ' + self.name + '\n\nТелефон: '  + self.phone + '\n\nИнтересует: ' + str(self.laptop)
        if new_creation:
            def telegram_bot_sendtext(bot_message):
                bot_token = '826322136:AAHRT7lDq3g3ykQ8Ms7CCXEpY8jD9qtUrro'
                # bot_token = '878082475:AAE8CiqE_-WGvLucDnEU13uJL0c4DsOry9k'
                bot_chatID = '-337321986'
                # bot_chatID = '-376800274'
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

                response = requests.get(send_text)

                return response.json()

            # send_mail(
            #     'UltraShop.uz: Поступила новая заявка от ' + self.name,
            #     message,
            #     'ikbolpm@gmail.com',
            #     ['ikbolpm@gmail.com',],
            #     fail_silently=False,
            # )

            telegram_bot_sendtext(message)


class ProductInquiry(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE, related_name='inquired_product')
    source = models.CharField(max_length=200)
    STATUS_CHOICES = (
        ('NOT_CONTACTED', 'Not Contacted'),
        ('ATTEMPTED_TO_CONTACT', 'Attempted to Contact'),
        ('ASKED_TO_CALL_LATER', 'Asked to Call Later'),
        ('DECISION_MAKING', 'Decision Making'),
        ('CLOSED_WON', 'Closed Won'),
        ('CLOSED LOST', 'Closed Lost')
    )
    description = models.TextField(default='Empty')
    status = models.CharField(choices=STATUS_CHOICES, default='NOT_CONTACTED', max_length=30)
    sold = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE, related_name='sold_product')

    class Meta:
        verbose_name_plural = 'Product Inquiries'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        new_creation = False
        if not self.id:
            new_creation = True
        super().save(force_insert, force_update, using, update_fields)
        message = 'Поступила новая заявка! Срочно позвоните! \n\nИмя: ' + self.name + '\n\nТелефон: '  + self.phone + '\n\nИнтересует: ' + str(self.product) + '\n\nЦена: $' + str(self.product.price)
        if new_creation:
            def telegram_bot_sendtext(bot_message):
                bot_token = '826322136:AAHRT7lDq3g3ykQ8Ms7CCXEpY8jD9qtUrro'
                # bot_token = '878082475:AAE8CiqE_-WGvLucDnEU13uJL0c4DsOry9k'
                bot_chatID = '-337321986'
                # bot_chatID = '-376800274'
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
                response = requests.get(send_text)
                return response.json()

        # send_mail(
        #     'UltraShop.uz: Поступила новая заявка от ' + self.name,
        #     message,
        #     'ikbolpm@gmail.com',
        #     ['ikbolpm@gmail.com',],
        #     fail_silently=False,
        # )

            telegram_bot_sendtext(message)