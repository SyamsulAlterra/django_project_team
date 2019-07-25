from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=255, help_text="Insert place name")
    description = models.TextField(max_length=1000, help_text="Insert place descriptions")
    maps = models.TextField(max_length=500, help_text='Only insert src script from html embed')

    def __str__(self):
        return self.name

class Photos(models.Model):
    # place_id = models.ForeignKey(Places.id, on_delete=models.CASCADE)
    place_name = models.ForeignKey(Places, on_delete=models.CASCADE)
    pic_url = models.CharField(max_length=2000)

    # def __str__(self):
    #     return self.place_name


class Review(models.Model):
    # place_id = models.ForeignKey(Places.id, on_delete=models.CASCADE)
    place_name = models.ForeignKey(Places, on_delete=models.CASCADE)
    review = models.TextField(max_length=500)

    # def __str__(self):
    #     return self.place_name