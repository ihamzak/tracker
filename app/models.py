from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class Expense(models.Model):
    expense_name = models.CharField(max_length=200)
    amount = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,to_field='category_name')

    def __str__(self):
        return self.expense_name

