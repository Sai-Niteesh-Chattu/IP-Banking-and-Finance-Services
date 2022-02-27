from django.contrib import admin
from transactions.models import Employee,Transactions,Status

# Register your models here.
admin.site.register(Transactions)
admin.site.register(Status)
admin.site.register(Employee)