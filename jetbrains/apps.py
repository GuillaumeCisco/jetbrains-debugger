from django.apps import AppConfig

from multiprocessing.managers import BaseManager

class ResourcesManager():
    pass

BaseManager.register('ResourcesManager', ResourcesManager)
manager = BaseManager()
manager.start()  # this line make debugger fail from 2019.2 pycharm versions

class JetbrainsConfig(AppConfig):
    name = 'jetbrains'

    def ready(self):
        print('foo')
        print('bar')
        print('baz')
