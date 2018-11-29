import json
from django.http import HttpResponse
from django.urls import resolve
from ..models import Bookmark
from ..forms import BookmarkForm

class BookmarkMixin:
    ''' Provides a BookmarkForm instance in the context '''
    bookmark_form = 'bookmark_form'

    def get_bookmark_form_name(self):
        return self.bookmark_form

    def get_context_data(self):
        context = super().get_context_data()
        match = resolve(self.request.path)
        initials = {
            'urlname': match.url_name,
            'args': match.args if match.args else None,
            'kwargs': match.kwargs if match.kwargs else None,
            'urlparams': self.request.GET.urlencode(),
        }
        context[self.get_bookmark_form_name()] = BookmarkForm(initial=initials)

        bm_id = self.request.GET.get('bm', None)
        if bm_id is not None:
            context['bookmark_exists'] = Bookmark.objects.filter(id=bm_id).exists()
            context['current_bm_id'] = bm_id
        return context


class JSONResponseMixin:
    def render_to_response(self, context):
        #"Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        #"Construct an `HttpResponse` object."
        return HttpResponse(content, content_type='application/json', **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        return json.dumps(context)
