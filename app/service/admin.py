from requests import Session

from app.database.session import Session as DatabaseSession
from app.database.models import User as UserModel
from app.api.requests import User as UserRequest
from app.serializers.user import UserApiKeyDetail, UserApiKeyCreate
from app.service.user import User


class Admin:
    """
        TODO: make Admin singleton?
        TODO: rename Admin to Service
    """
    def __init__(self):
        self.session = Session()
        self.session.headers['Content-Type'] = 'application/json'

    def user_get_or_create(self, telegram):
        database_session = DatabaseSession()
        user_object = database_session.query(UserModel).filter_by(telegram=telegram).first()

        if user_object is None:
            username = f'telegram_{telegram}'

            # Prepare user data for registration
            user_data = UserApiKeyCreate(
                username=username,
            )

            # Send user registration request
            request = self.session.prepare_request(UserRequest.create(json=user_data.dict()))
            response = self.session.send(request)

            if response.status_code != 201:
                # TODO: verify somehow request exceptions and status code
                pass

            # TODO: verify somehow validation exceptions
            validated_data = UserApiKeyDetail.parse_raw(response.text)

            # Save new user to database
            user_object = UserModel(
                telegram=telegram,
                username=username,
                api_key=validated_data.api_key,
            )
            database_session.add(user_object)
            database_session.commit()

        user = User(user_object.api_key)
        database_session.close()

        # TODO: Check that user api_key is valid by sending an test request

        return user
