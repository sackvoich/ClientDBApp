from django.db import models

class Order(models.Model):
    employee_name = models.CharField(max_length=100, verbose_name='Фамилия сотрудника')
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма заказа')
    product_name = models.CharField(max_length=200, verbose_name='Наименование товара')
    client_company = models.CharField(max_length=200, verbose_name='Название фирмы-клиента')
    customer_name = models.CharField(max_length=100, verbose_name='Фамилия заказчика')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')

    def __str__(self):
        return f"Заказ №{self.id} - {self.product_name} ({self.client_company})"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'