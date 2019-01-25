import random
from rango.models import Category, Page
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rango_project.settings')

django.setup()


def add_cat(lst):
    c = Category.objects.get_or_create(name=lst[0])[0]
    c.views = lst[1]
    c.likes = lst[2]
    c.save()
    return c


lst = [["Python", 128, 64], ["Django", 64, 32], ["Other Frameworks", 32, 16]]
for l in lst:
    add_cat(l)
for i in range(1, 9):
    p = Page.objects.get_or_create(id=i)[0]
    r = random.randint(50, 100)
    p.views = r
    p.save()
