=====
Bookmarks
=====

Bookmarks is a simple Django app to save in app urls as bookmarks.

Quick start
-----------

1. Add "bookmarks" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bookmarks',
    ]

2. Include the bookmarks URLconf in your project urls.py like this::

    path('boookmarks/', include('bookmarks.urls')),

3. Run `python manage.py migrate` to create the bookmarks models.

4. Extend the view you intend to use bookmarks in with the provided mixin::
    
    from bookmarks.views import BookmarkMixin
    
    class MyModelView(BookmarkMixin):
        template_name = 'mymodeltemplate.html'
        # do stuff ...

5. Include bookmark template inside the template you defined in the view::
    ...
    {% include 'bookmarks/bookmark_form.html' %}

7. Visit http://127.0.0.1:8000/ to start creating bookmarks.
