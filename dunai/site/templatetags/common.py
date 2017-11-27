from django.template import Library
from django.utils.html import mark_safe
from django.contrib.staticfiles.templatetags.staticfiles import static

register = Library()


ICONS = {
    'python': 'python-plain colored',
    'js': 'javascript-plain colored',
    'nodejs': 'nodejs-plain colored',
    'web': 'chrome-plain colored',
    'docker': 'docker-plain colored',
    'aws': 'amazonwebservices-original colored',
    'mongodb': 'mongodb-plain colored',
    'postgresql': 'postgresql-plain colored',
    'mysql': 'mysql-plain colored',
    'c': 'c-plain colored',
    'c++': 'cplusplus-plain colored',
    'django': 'django-plain',
    'backbone': 'backbonejs-plain',
    'java': 'java-plain colored',
    'php': 'php-plain colored',
    'c#': 'csharp-plain colored',
    'linux administration': 'linux-plain',
    'heroku': 'heroku-plain colored',
    'android': 'android-plain colored',
    'redis': 'redis-plain colored',
    'default': 'linux-plain',
}

SVG_ICONS = {
    'qt': (static('svg/qt.svg'), '#7EC040'),
    'ms sql': (static('svg/sql-server.svg'), '#FFFFFF'),
    'sip': (static('svg/asterisk.png'), '#EE610D'),
    'flask': (static('svg/flask.svg'), '#FFFFFF'),
    'gtk': (static('svg/gtk.svg'), '#7FE719'),
    'solr': (static('svg/solr.svg'), '#D74125'),
    'rabbitmq': (static('svg/rabbitmq.svg'), '#FC6401'),
    'consul': (static('svg/consul.svg'), '#C62A71'),
    'microservices': (static('svg/microservices.svg'), '#A21A86'),
    'service architecture': (static('svg/microservices.svg'), '#A21A86'),
    'networking & security': (static('svg/network.svg'), '#FBDD4E'),
    'twisted': (static('svg/twisted.svg'), '#FFFFFF'),
}


@register.filter
def icon(t):
    img_pat = \
        '<img src="{}" class="icon" title="' + t + '" />'
    icon_pat = \
        '<i class="devicon-{} icon" title="' + t + '"></i>'
    t = t.lower()
    result = None

    if t in SVG_ICONS:
        result = img_pat.format(*SVG_ICONS[t])
    elif t in ICONS:
        result = icon_pat.format(ICONS[t])
    else:
        result = icon_pat.format(ICONS['default'])

    return mark_safe(result)

