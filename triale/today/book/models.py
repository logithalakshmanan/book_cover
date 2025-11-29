from django.db import models

class book(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField
    book_model= models.CharField(max_length=20)
    book_no= models.CharField(max_length=100)
    book_name= models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    Phone_no=models.CharField(max_length=15)

class bookAdmin(admin.ModelAdmin):
    list_display=('Name','Email','book_model','book no','book name','address','Phone_no')
