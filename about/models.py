from django.db import models


class CompanyInfo(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mission_statement = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'CompanyInfo'
        ordering = ('title', )

    def __str__(self):
        return f'{self.title}'


class TeamMember(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=250)


    class Meta:
        verbose_name_plural = 'Teammember'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'