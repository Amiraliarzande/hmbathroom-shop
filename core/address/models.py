from django.db import models
from django.conf import settings


class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='addresses'
    )
    label = models.CharField('Address label', max_length=100, help_text='e.g. Home, Work')
    full_name = models.CharField('Full name', max_length=150)
    address_line_1 = models.CharField('Address line 1', max_length=255)
    address_line_2 = models.CharField('Address line 2', max_length=255, blank=True, null=True)
    city = models.CharField('Town / City', max_length=100)
    postcode = models.CharField('Postcode', max_length=20)
    country = models.CharField('Country', max_length=100, default='United Kingdom')
    phone = models.CharField('Contact number', max_length=20, blank=True, null=True)
    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.label} - {self.city} ({self.user.email})"

    def save(self, *args, **kwargs):
        if self.is_default:
            Address.objects.filter(user=self.user, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['-is_default', '-created_at']