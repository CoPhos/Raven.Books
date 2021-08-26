from django.db import models
from django.utils import timezone

# Create your models here.
class Review(models.Model):
    tittle = models.CharField(max_length=255, null=False, blank=False)
    date_created = models.DateTimeField(default=timezone.now)
    text = models.TextField(null=False, blank=False)
    customer = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name="review_customer")
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name="review_book")
    
    def __str__(self):
        return self.tittle

class Score(models.Model):
    score = models.DecimalField(max_digits=2, decimal_places=1, null=False, blank=False)
    customer = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name="score_customer")
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name="score_book")