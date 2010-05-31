from django.conf import settings

# A few aliases, because there's FQMNs now in 1.2.
engine_modules = {
    'django.db.backends.postgresql_psycopg2': 'postgresql_psycopg2',
    'django.db.backends.sqlite3': 'sqlite3',
    'django.db.backends.mysql': 'mysql',
    'django.db.backends.oracle': 'oracle',
    'django.db.backends.sql_server.pyodbc': 'sql_server.pyodbc',
    'django.contrib.gis.db.backends.postgis': 'postgresql_psycopg2',
    'django.contrib.gis.db.backends.spatialite': 'sqlite3',
    'django.contrib.gis.db.backends.mysql': 'mysql',
    'django.contrib.gis.db.backends.oracle': 'oracle',
}

if getattr(settings, 'DATABASE_ENGINE', False):
    # Pre 1.2
    db_engine = settings.DATABASE_ENGINE
else:
    try:
       db_engine = engine_modules[settings.DATABASES['default']['ENGINE']]
    except KeyError:
       # Simple let the import fail by using an invalid module name
       db_engine = 'df'

triggers_module_name = ['denorm.db', db_engine, 'triggers']
try:
    triggers = __import__('.'.join(triggers_module_name),{},{},[''])
except ImportError:
    raise ImportError("There is no django-denorm database module for the engine '%s'. Please either choose a supported one, or remove 'denorm' from INSTALLED_APPS.\n" % settings.DATABASE_ENGINE)

del db_engine
