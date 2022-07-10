from django.db import models

# Create your models here.
class WikiFolder(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class WikiBase(models.Model):
    title = models.CharField(max_length=255)

    folder = models.ForeignKey(
        'WikiFolder',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

class WikiContent(models.Model):
    content = models.TextField()
    author_id = models.IntegerField()
    approved = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    base = models.ForeignKey(
        'WikiBase',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.base.title