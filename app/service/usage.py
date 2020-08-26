from app.service import Admin


admin = Admin()

telegram_id = 68376429784
user = admin.user_get_or_create(telegram=telegram_id)
