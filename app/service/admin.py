from typing import Dict

from apiclient.client import APIClient
from apiclient.authentication_methods import NoAuthentication
from apiclient.exceptions import ClientError

from app.database.session import Session
from app.database.models import User
from app.service.endpoints import EndpointUser
from app.service.user import APIUser

from app.serializers.user import UserApiKeyDetail, UserApiKeyCreate


class APIAdmin(APIClient):
    def __init__(self):
        super().__init__(
            authentication_method=NoAuthentication(),
        )

    def user_check(self, username: str):
        return self.post(endpoint=EndpointUser.user_check, data={'username': username})

    def user_create(self, username: str):
        return self.post(endpoint=EndpointUser.user_create, data={'username': username})

    def user_restore(self, username: str):
        return self.post(endpoint=EndpointUser.user_restore, data={'username': username})

    def user_client_get_or_create(self, telegram):
        with Session() as database_session:
            user_object = database_session.query(User).filter_by(telegram=telegram).first()

            # If user exist
            if user_object is not None:
                pass

            # If user doesn't exist...
            if user_object is None:
                username = f'telegram_{telegram}'

                # Send user registration request
                try:
                    response = self.user_create(username)
                except ClientError:
                    response = self.user_restore(username)

                print(response)
                print(response.text)

                # TODO: verify somehow validation exceptions
                validated_data = UserApiKeyDetail.parse_raw(response.text)

                # Save new user to database
                user_object = User(
                    telegram=telegram,
                    username=username,
                    api_key=validated_data.api_key,
                )
                database_session.add(user_object)
                database_session.commit()

            api_user = APIUser(api_key=user_object.api_key)
            database_session.close()

            # TODO: Check that user api_key is valid by sending an test request

            return api_user


admin = APIAdmin()

user = admin.user_client_get_or_create(telegram='123456789')
if user is None:
    print('Exception')
