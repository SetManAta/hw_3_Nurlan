from django.db import models


class Client(models.Model):

    
    name = models.CharField(max_length=20, verbose_name='Имя',null=False,blank=False)
    citizenship = models.CharField(max_length=20, verbose_name ='гражданство', null=False,default='Кыргызстан') 
    birth_year = models.DateField(null=False,blank=False,verbose_name='год рождения') 
    work_place =  models.CharField(max_length = 30, verbose_name= 'место работы', null=True, blank=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.name}'

class Account(models.Model):
    number = models.CharField(max_length=16, verbose_name='номер аккаунта',primary_key=True,null=False,blank=False)
    account_type = models.IntegerField(verbose_name='тип аккаунта', default=1,null=False,blank=False) 
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Счет'
        verbose_name_plural =  'Счета'

    def __str__(self):
        return f'Номер счета - {self.number}'
    

class Credit(models.Model):

    sum = models.IntegerField(verbose_name='сумма кредита',null=False,blank=False)
    date = models.DateField(auto_now_add=True, verbose_name='Дата получения кредита')
    account = models.ForeignKey(Account, related_name='credits',on_delete=models.CASCADE,verbose_name='Счет')

    class Meta:
        db_table = 'loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'

    def __str__(self):
        return f'Сумма кредита - {self.sum}'

    