# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.urls import reverse


class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_bookmarks")
    name = models.CharField(max_length=30)
    urlname = models.CharField(max_length=100)
    args = models.CharField(max_length=100, blank=True, null=True)
    kwargs = models.CharField(max_length=100, blank=True, null=True)
    urlparams = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['name']
        permissions = (
            ('manage_bookmarks', 'Add and remove bookmarks'),
        )

    def __str__(self):
        return self.name

    def get_bookmark_url(self):
        url = reverse(self.urlname, args=self.args, kwargs=self.kwargs)
        if self.urlparams:
            url = url + '?' + self.urlparams
        return url
