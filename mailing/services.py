from django.core.cache import cache
from django.shortcuts import get_object_or_404

from mailing.models import Client
# from config.settings import CACHE_ENABLED


def set_owner(self, form, object_is_new=True):

    self.object = form.save()

    if object_is_new:
        self.object.owner = self.request.user
        self.object.save()


def check_user_is_owner_or_su(self, model_):
    pk = self.kwargs.get('pk')
    object_ = get_object_or_404(model_, pk=pk)
    return (self.request.user == object_.owner) or self.request.user.is_superuser
