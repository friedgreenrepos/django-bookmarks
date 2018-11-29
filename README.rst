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

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a Bookmark (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ to start creating bookmarks.
