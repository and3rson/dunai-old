import re
import json
import time
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

from django.db import models
from ordered_model.models import OrderedModel


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def cached_model_method(ttl):
    def decorator(fn):
        fn.caches = {}
        fn.ttl = ttl
        def wrapper(self, *args, **kwargs):
            if self.id not in fn.caches:
                fn.caches[self.id] = dict(
                    last_call=None,
                    value=None
                )
            cache = fn.caches[self.id]
            if cache['last_call'] is None or cache['last_call'] + fn.ttl < time.time():
                cache['last_call'] = time.time()
                cache['value'] = fn(self, *args, **kwargs)
            return cache['value']
        return wrapper
    return decorator


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
    stars = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return u'{} ({})'.format(self.title, self.link)

    def get_stars(self):
        match = re.match('.*github\.com/([a-zA-Z0-9_\.-]+)/([a-zA-Z0-9_\.-]+)', self.link)
        try:
            if match:
                user, repo = match.groups()
                response = urlopen('https://github.com/{}/{}/network'.format(user, repo), context=ctx)
                doc = BS(response.read(), 'html.parser')
                count = [el for el in doc.select('.social-count') if 'stargazers' in el['href']][0]
                return int(count.text.strip().replace(',', ''))
                # response = urlopen('https://api.github.com/repos/{}/{}'.format(user, repo), context=ctx)
                # return json.loads(response.read())['stargazers_count']
        except Exception as e:
            return 'Error: {}'.format(str(e))
        return

    def update_stars(self):
        self.stars = self.get_stars()

    __repr__ = __str__
