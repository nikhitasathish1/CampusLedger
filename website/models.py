from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    phone_no= models.CharField(max_length=12)
    email= models.CharField(max_length=50)
    city= models.CharField(max_length=20)
    state= models.CharField(max_length=20)
    zipcode= models.CharField(max_length=7)
    
    def __str__(self):
        return(f"{self.first_name}{self.last_name}")
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_borrowed = models.DateField()
    date_returned = models.DateField(null=True, blank=True)
    
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name="books")
def __str__(self):
        return f"{self.title} by {self.author}"
    
