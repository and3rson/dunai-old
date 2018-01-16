from django.db import models
from ordered_model.models import OrderedModel


class Feature(OrderedModel):
    class Meta(OrderedModel.Meta):
        pass

    photo = models.ImageField(null=False, blank=False, upload_to='photos')
    location = models.TextField(null=True, blank=True)
    comment = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.comment

    __repr__ = __str__

