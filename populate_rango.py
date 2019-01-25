from rango.models import Category, Page
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rango_project.settings')

django.setup()


def populate():
    python_pages = [
        {"titile": "Official Python Tutorial",
            "url": "http://docs.python.org/2/tutorial/"},

        {"titile": "How to Think like a Computer Scientist",
            "url": "http://www.greenteapress.com/thinkpython/"},
        {"titile": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}]

    django_pages = [
        {"titile": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"titile": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"titile": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}]

    other_pages = [
        {"titile": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"titile": "Flask",
         "url": "http://flask.pocoo.org"}]

    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages}}
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["titile"], p["url"])

    for c in Category.objects.all():
        for p in Page.objects.filter(Category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, titile, url, views=0):
    p = Page.objects.get_or_create(Category=cat, titile=titile)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c
    # Start execution here!


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
