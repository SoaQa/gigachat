from django.views import generic

from api.models import UserProfile


class UserView(generic.ListView):
    model = UserProfile
