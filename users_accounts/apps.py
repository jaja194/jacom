from django.apps import AppConfig


class UsersAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_accounts'

    #def ready(self):
    #    import users_accounts.signals
