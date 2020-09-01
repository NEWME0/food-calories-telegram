from requests import Request

from app.api.mixins import RequestSet, RetrieveImplicitMixin, UpdateImplicitMixin, DestroyImplicitMixin
from app.config import BASE_URL


class FoodPortion(RequestSet):
    base = BASE_URL
    path = '/api/food/portion/'


class FoodCategory(RequestSet):
    base = BASE_URL
    path = '/api/food/category/'


class Food(RequestSet):
    base = BASE_URL
    path = '/api/food/'


class Activity(RequestSet):
    base = BASE_URL
    PATH = '/api/activity/'


class FoodJournal(RequestSet):
    base = BASE_URL
    path = '/track/food/'


class ActivityJournal(RequestSet):
    base = BASE_URL
    path = '/track/activity/'


class User:
    """
        POST    /user/apikey/new/     user_apikey_new_create
        PUT     /user/apikey/update/  user_apikey_update_update
        DELETE  /user/apikey/update/  user_apikey_update_delete
        POST    /user/recovery/       user_recovery_create
    """

    base = BASE_URL
    path = '/user/apikey/new/'

    @classmethod
    def create(cls, json):
        return Request('POST', f'{cls.base}/user/apikey/new/', json=json)


class UserDetail(RetrieveImplicitMixin, UpdateImplicitMixin, DestroyImplicitMixin):
    base = BASE_URL
    path = '/user/detail/'


class UserProfile(RetrieveImplicitMixin, UpdateImplicitMixin):
    base = BASE_URL
    path = '/user/profile/'


class UserTarget(RetrieveImplicitMixin, UpdateImplicitMixin):
    base = BASE_URL
    path = '/user/target/'
