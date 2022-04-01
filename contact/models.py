from django.db import models


class Contact(models.Model):
    """ Contact Model for Contact Form """

    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    message = models.TextField(max_length=500, null=False, blank=False)
    order_number = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    def email(self):
        return self.email
