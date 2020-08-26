from requests import Session


class User:
    session: Session = None

    def __init__(self, api_key):
        self.session = Session()
        self.session.headers['X-Api-Key'] = api_key
        self.session.headers['Content-Type'] = 'application/json'

    def food_activity_list(self):
        raise NotImplementedError()

    def food_activity_create(self, json):
        raise NotImplementedError('')

    def food_activity_retrieve(self, item_id):
        raise NotImplementedError('')

    def food_activity_update(self, item_id, json):
        raise NotImplementedError('')

    def food_activity_destroy(self, item_id):
        raise NotImplementedError('')
