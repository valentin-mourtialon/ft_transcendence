# class MyDBRouter:
#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read models go to the secondary database.
#         """
#         if model._meta.app_label == 'prometheus':
#             return 'prometheus'
#         return 'default'

#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write models go to the default database.
#         """
#         if model._meta.app_label == 'prometheus':
#             return 'prometheus'
#         return 'default'

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the 'your_app_name' app is involved.
#         """
#         if obj1._meta.app_label == 'prometheus' or \
#            obj2._meta.app_label == 'prometheus':
#            return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Ensure that the 'your_app_name' app's models get created on the right database.
#         """
#         if app_label == 'prometheus':
#             return db == 'prometheus'
#         return db == 'default'