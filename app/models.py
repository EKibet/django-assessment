from django.db import models

# Create your models here.
class CommonFieldsMixin(models.Model):
    """
    This contains all common fields
    Every model will inherit this to ensure DRY code
    Its abstract hence can't be instatiated
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ['-updated_at', '-created_at']
        abstract = True
class Points(CommonFieldsMixin):
    """
    This is the schema for saving the following:
    values:
        # -The string of points submitted 
        # -The result of the computation: the closest points pair 
    """
    points_submitted=models.CharField(max_length=255)
    closest_point=models.CharField(max_length=255)
    relative_point= models.CharField(max_length=255,null=True)


