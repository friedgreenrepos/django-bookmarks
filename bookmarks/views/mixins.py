import json
from django.http import HttpResponse
from django.urls import resolve
from ..models import Bookmark
from ..forms import BookmarkForm
from ..settings import BUTTON_TEXT_SAVE, BUTTON_TEXT_DELETE
from .. import utils


class BookmarkMixin:
    ''' Provide a BookmarkForm instance in the context '''
    bookmark_form = 'bookmark_form'

    def get_bookmark_form_name(self):
        return self.bookmark_form

    def get_context_data(self):
        context = super().get_context_data()
        context['button_text'] = BUTTON_TEXT_SAVE
        context['bookmark_exists'] = False
        match = resolve(self.request.path)
        params = self.request.GET.urlencode()
        if params:
            context['bookmark_bnt_visible'] = True
            initials = {
                'urlname': match.url_name,
                'args': match.args if match.args else None,
                'kwargs': match.kwargs if match.kwargs else None,
                'urlparams': params,
            }
            context[self.get_bookmark_form_name()] = BookmarkForm(initial=initials)

            filters = {
                'user': self.request.user,
                'urlname': match.url_name,
                'args': match.args if match.args else None,
                'kwargs': match.kwargs if match.kwargs else None,
            }
            for bm in Bookmark.objects.filter(**filters):
                params_dict = utils.params_to_dict(bm.urlparams)
                if cmp(params_dict, self.request.GET.dict()) ==  0:
                    context['bookmark_exists'] = True
                    context['current_bm_id'] = bm.id

            if context['bookmark_exists']:
                context['button_text'] = BUTTON_TEXT_DELETE
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
