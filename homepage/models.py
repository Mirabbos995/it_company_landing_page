from django.db import models



class Service(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Services'
        ordering = ('title',)

    def __str__(self):
        return self.title

class Ideas(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Ideas'
        ordering = ('name',)


    def __str__(self):
        return self.name

class ProcessStep(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Processstep'
        ordering = ('title',)
    def __str__(self):
        return self.title