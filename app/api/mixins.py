from abc import ABC
from requests import Request


class ListMixin(ABC):
    @classmethod
    def list(cls):
        return Request('GET', f'{cls.base}{cls.path}')


class CreateMixin(ABC):
    @classmethod
    def create(cls, json):
        return Request('POST', f'{cls.base}{cls.path}', json=json)


class RetrieveMixin(ABC):
    @classmethod
    def retrieve(cls, item_id):
        return Request('GET', f'{cls.base}{cls.path}{item_id}/')


class UpdateMixin(ABC):
    @classmethod
    def update(cls, item_id, json):
        return Request('PUT', f'{cls.base}{cls.path}{item_id}/', json=json)

    @classmethod
    def partial_update(cls, item_id, json):
        return Request('PATCH', f'{cls.base}{cls.path}{item_id}/', json=json)


class DestroyMixin(ABC):
    @classmethod
    def destroy(cls, item_id):
        return Request('DELETE', f'{cls.base}{cls.path}{item_id}/')


class RequestSet(ListMixin, CreateMixin, RetrieveMixin, UpdateMixin, DestroyMixin, ABC):
    """ All requests """


class RetrieveImplicitMixin(ABC):
    @classmethod
    def retrieve(cls):
        return Request('GET', f'{cls.base}{cls.path}')


class UpdateImplicitMixin(ABC):
    @classmethod
    def update(cls, json):
        return Request('PUT', f'{cls.base}{cls.path}', json=json)


class DestroyImplicitMixin(ABC):
    @classmethod
    def destroy(cls):
        return Request('DELETE', f'{cls.base}{cls.path}')
