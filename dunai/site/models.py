from django.db import models
from ordered_model.models import OrderedModel


class Feature(OrderedModel):
    class Meta(OrderedModel.Meta):
        pass

    photo = models.ImageField(null=False, blank=False, upload_to='photos')
    location = models.TextField(null=True, blank=True)
    comment = models.TextField(null=False, blank=False)

    def __str__(self):
        return u'{} ({})'.format(self.comment, self.location)

    __repr__ = __str__


class Project(OrderedModel):
    class Meta(OrderedModel.Meta):
        pass

    title = models.TextField(null=False, blank=False)
    link = models.URLField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return u'{} ({})'.format(self.title, self.link)

    __repr__ = __str__
