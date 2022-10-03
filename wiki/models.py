from django.db import models

class WikiBase(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=520)

    def __str__(self):
        return self.title

class WikiContent(models.Model):
    content = models.TextField()
    author_id = models.IntegerField()
    is_approved = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    base = models.ForeignKey(
        'WikiBase',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.base.title