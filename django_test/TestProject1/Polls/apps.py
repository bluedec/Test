#AppConfig represents a django application and it's configuration
#We import it, to give it to the class of the app.
from django.apps import AppConfig


#class represents the config of the app
class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Polls'
