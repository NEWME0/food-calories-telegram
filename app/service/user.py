from requests import Session

from app.api import requests
from app.serializers import activity, food, journal, search, user


class User:
    session: Session = None

    def __init__(self, api_key):
        self.session = Session()
        self.session.headers['X-Api-Key'] = api_key
        self.session.headers['Content-Type'] = 'application/json'

    def _request(self, request, serializer):
        request = self.session.prepare_request(request)
        response = self.session.send(request)

        if serializer is not None:
            validated_data = serializer.parse_raw(response.text)
            return validated_data

    def food_portion_list(self):
        request = requests.FoodPortion.list()
        serializer = food.FoodPortionList
        return self._request(request, serializer)

    def food_portion_create(self, json):
        request = requests.FoodPortion.create(json=json)
        serializer = food.FoodPortionCreate
        return self._request(request, serializer)

    def food_portion_retrieve(self, item_id):
        request = requests.FoodPortion.retrieve(item_id=item_id)
        serializer = food.FoodPortionDetail
        return self._request(request, serializer)

    def food_portion_update(self, item_id, json):
        request = requests.FoodPortion.update(item_id=item_id, json=json)
        serializer = food.FoodPortionCreate
        return self._request(request, serializer)

    def food_portion_destroy(self, item_id):
        request = requests.FoodPortion.destroy(item_id=item_id)
        serializer = None
        return self._request(request, serializer)

    def food_category_list(self):
        request = requests.FoodCategory.list()
        serializer = food.FoodCategoryList
        return self._request(request, serializer)

    def food_category_create(self, json):
        request = requests.FoodCategory.create(json=json)
        serializer = food.FoodCategoryCreate
        return self._request(request, serializer)

    def food_category_retrieve(self, item_id):
        request = requests.FoodCategory.retrieve(item_id=item_id)
        serializer = food.FoodCategoryDetail
        return self._request(request, serializer)

    def food_category_update(self, item_id, json):
        request = requests.FoodCategory.update(item_id=item_id, json=json)
        serializer = food.FoodCategoryCreate
        return self._request(request, serializer)

    def food_category_destroy(self, item_id):
        request = requests.FoodCategory.destroy(item_id=item_id)
        serializer = None
        return self._request(request, serializer)

    def food_list(self):
        request = requests.Food.list()
        serializer = food.FoodList
        return self._request(request, serializer)

    def food_create(self, json):
        request = requests.Food.create(json)
        serializer = food.FoodCreate
        return self._request(request, serializer)

    def food_retrieve(self, item_id):
        request = requests.Food.retrieve(item_id=item_id)
        serializer = food.FoodDetail
        return self._request(request, serializer)

    def food_update(self, item_id, json):
        request = requests.Food.update(item_id=item_id, json=json)
        serializer = food.FoodCreate
        return self._request(request, serializer)

    def food_destroy(self, item_id):
        request = requests.Food.destroy(item_id=item_id)
        serializer = None
        return self._request(request, serializer)

    def activity_list(self):
        request = requests.Activity.list()
        serializer = activity.ActivityList
        return self._request(request, serializer)

    def activity_create(self, json):
        request = requests.Activity.create(json=json)
        serializer = activity.ActivityCreate
        return self._request(request, serializer)

    def activity_retrieve(self, item_id):
        request = requests.Activity.retrieve(item_id=item_id)
        serializer = activity.ActivityDetail
        return self._request(request, serializer)

    def activity_update(self, item_id, json):
        request = requests.Activity.update(item_id=item_id, json=json)
        serializer = activity.ActivityCreate
        return self._request(request, serializer)

    def activity_destroy(self, item_id):
        request = requests.Activity.destroy(item_id=item_id)
        serializer = None
        return self._request(request, serializer)

    def journal_food_list(self):
        request = requests.FoodJournal.list()
        serializer = journal.FoodJournalList
        return self._request(request, serializer)

    def journal_food_create(self, json):
        request = requests.FoodJournal.create(json=json)
        serializer = journal.FoodJournalCreate
        return self._request(request, serializer)

    def journal_food_retrieve(self, item_id):
        request = requests.FoodJournal.retrieve(item_id=item_id)
        serializer = journal.FoodJournalDetail
        return self._request(request, serializer)

    def journal_food_update(self, item_id, json):
        request = requests.FoodJournal.update(item_id=item_id, json=json)
        serializer = journal.FoodJournalCreate
        return self._request(request, serializer)

    def journal_food_destroy(self, item_id):
        request = requests.FoodJournal.destroy(item_id=item_id)
        serializer = None
        return self._request(request, serializer)

    def journal_activity_list(self):
        request = requests.ActivityJournal.list()
        serializer = journal.ActivityJournalList
        return self._request(request, serializer)

    def journal_activity_create(self, json):
        request = requests.ActivityJournal.create(json=json)
        serializer = journal.ActivityJournalCreate
        return self._request(request, serializer)

    def journal_activity_retrieve(self, item_id):
        request = requests.ActivityJournal.retrieve(item_id=item_id)
        serializer = journal.ActivityJournalDetail
        return self._request(request, serializer)

    def journal_activity_update(self, item_id, json):
        request = requests.ActivityJournal.update(item_id=item_id, json=json)
        serializer = journal.ActivityJournalCreate
        return self._request(request, serializer)

    def journal_activity_destroy(self, item_id):
        request = requests.ActivityJournal.destroy(item_id=item_id)
        serializer = None
        return self._request(request, serializer)

    def journal_status_retrieve(self):
        raise NotImplementedError('')

    def profile_retrieve(self):
        request = requests.UserProfile.retrieve()
        serializer = user.UserProfile
        return self._request(request, serializer)

    def profile_update(self):
        raise NotImplementedError('')

    def target_retrieve(self):
        raise NotImplementedError('')

    def target_update(self):
        raise NotImplementedError('')
