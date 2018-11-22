# api/models.py

from django.db import models
class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner_id = models.ForeignKey('auth.User',
    related_name='bucketlists', 
    on_delete=models.CASCADE, default=1) 

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

    class Meta:
        db_table = 'techno_bucketlist'