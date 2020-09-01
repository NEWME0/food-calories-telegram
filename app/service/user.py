from apiclient import APIClient, HeaderAuthentication, JsonResponseHandler, JsonRequestFormatter
from app.service.endpoints import EndpointUser


class APIUser(APIClient):
    def __init__(self, api_key):
        authentication_method = HeaderAuthentication(
            token=api_key,
            parameter='X-Api-Key',
            scheme='',
        )

        super().__init__(
            authentication_method=authentication_method,
            response_handler=JsonResponseHandler,
            request_formatter=JsonRequestFormatter,
        )

    def check(self):
        self.get(endpoint=EndpointUser.check)
