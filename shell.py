from random import randint
from credit.models import Account, Credit, Client

def random(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)



client1 = Client.objects.create(name="Бердиев Н.Д.", birth_year='1994-10-10',work_place='Codyfi')
client2 = Client.objects.create(name="Жамбулат Ж.Ж.", birth_year='1990-5-10',work_place='Googlejam')

account1 = client1.accounts.create(number=random(16))
account2 = client1.accounts.create(number=random(16),account_type=2)
account3 = client2.accounts.create(number=random(16),account_type=3)
account4 = client2.accounts.create(number=random(16),account_type=4)


credit1 = account1.credits.create(sum=10000)
credit2 = account2.credits.create(sum=20000)
credit3 = account3.credits.create(sum=30000)
credit4 = account4.credits.create(sum=40000)




