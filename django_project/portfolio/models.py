from django.db import models

# Create your models here. The data from the search is saved in MySQL database
class search_info(models.Model):
                              #choices
                              text_search = models.CharField(max_length=100)
                              year_search = models.PositiveSmallIntegerField(blank=True, null=True)

