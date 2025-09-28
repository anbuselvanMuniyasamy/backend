from django.apps import AppConfig


class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'
<<<<<<< HEAD


    def ready(self):
        import inventory.signals
=======
>>>>>>> 0058cfcddd355e69c1d8cea8f79bf7aa2579ae46
