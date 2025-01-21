from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100) # Har bir <li> ichidagi matn
    created_at = models.DateTimeField(auto_now_add=True) # Qo'shilgan sana vaqt

    def __str__(self):
        return self.name
    