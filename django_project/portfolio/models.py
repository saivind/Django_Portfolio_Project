from django.db import models

# Create your models here.
class search_info(models.Model):
                              #choices
                              text_search = models.CharField(max_length=100)
                              year_search = models.PositiveSmallIntegerField(blank=True, null=True)

