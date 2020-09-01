from apiclient.decorates import endpoint


BASE_URL = 'https://track-calorie.curs-valutar.xyz/'


@endpoint(base_url=BASE_URL)
class EndpointUser:
    user_check = '/user/check/'
    user_create = '/user/apikey/new/'
    user_restore = '/user/restore/'

