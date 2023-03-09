from django.db import models

class Subcriber(models.Model):
    email = models.EmailField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class MailMessage(models.Model):
    title = models.CharField(max_length=150, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title