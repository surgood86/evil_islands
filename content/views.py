from django.views import generic
from .models import Content


class ContentListViews(generic.ListView):
    template_name = "base.html"
    context_object_name = "content"
    model = Content

    #def get(self, request, *args, **kwargs):
    #    pass
#
    #def get_context_data(self, *, object_list=None, **kwargs):
    #    pass
#