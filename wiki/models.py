from django.db import models

class Wiki(models.Model):
    title = models.CharField(unique=True, max_length=255)
    tags = models.CharField(max_length=520)
    content = models.TextField()    
    author_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
