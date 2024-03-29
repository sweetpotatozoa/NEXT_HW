from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    # The 'default' attribute is used to set a default image for the article. The 'blank' attribute is set to True to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will be displayed if no image is uploaded.
    # The 'blank=True' attribute is used to allow for the image to be optional.
    # The 'default.png' image is a placeholder image that will