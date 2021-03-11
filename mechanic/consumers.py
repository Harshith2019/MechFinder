import json
from .models import users
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from channels.generic.websocket import WebsocketConsumer

instances = []

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        global instances

        instances.append(self)

        self.send(json.dumps({'message': users.get_all_objects(users)}))

    def disconnect(self, close_code):

        global instances

        instances.remove(self)

        self.close()


@receiver(post_save, sender=users)
@receiver(post_delete, sender=users)
def get_model_objects(sender, **kwargs):
    print(users.get_all_objects(users))

    for instance in instances:
        instance.send(json.dumps({'message': users.get_all_objects(users)}))
