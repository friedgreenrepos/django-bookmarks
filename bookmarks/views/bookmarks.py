from django.http import HttpResponseNotAllowed
from django.db import transaction
from django.views.generic import CreateView, DeleteView, View
from ..models import Bookmark
from ..forms import BookmarkForm
from .mixins import JSONResponseMixin


class CreateBookmarkView(CreateView):
    model = Bookmark
    form_class = BookmarkForm

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_bookmark_url()


class DeleteBookmarkView(JSONResponseMixin, View):
    model = Bookmark

    def post(self, request, *args, **kwargs):
        bmid = request.POST.get('bmid', None)
        if bmid is not None:
            try:
                bm = Bookmark.objects.get(id=bmid)
            except Bookmark.DoesNotExist:
                bm = None

        if bm is not None:
            bm.delete()
        context = {}
        return self.render_to_response(context)
