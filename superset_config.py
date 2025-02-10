import os
import logging
from dotenv import load_dotenv
from flask_appbuilder.security.manager import AUTH_OAUTH

# Configurar logging para depuración
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY', 'default-secret-key')

# Habilitar OAuth
AUTH_TYPE = AUTH_OAUTH
LOGOUT_REDIRECT_URL = f"{os.getenv('KEYCLOAK_SERVER')}/realms/{os.getenv('KEYCLOAK_REALM')}/protocol/openid-connect/logout"
AUTH_USER_REGISTRATION = True
AUTH_ROLES_SYNC_AT_LOGIN = True

OAUTH_PROVIDERS = [
    {
        'name': 'keycloak',
        'icon': 'fa-key',
        'token_key': 'access_token',
        'remote_app': {
            'client_id': os.getenv('KEYCLOAK_CLIENT_ID'),
            'client_secret': os.getenv('KEYCLOAK_CLIENT_SECRET'),
            'client_kwargs': {
                'scope': 'openid profile email',
            },
            'server_metadata_url': f"{os.getenv('KEYCLOAK_SERVER')}/realms/{os.getenv('KEYCLOAK_REALM')}/.well-known/openid-configuration",
        },
    }
]

# Asignación de roles de Keycloak a Superset
AUTH_ROLES_MAPPING = {
    "Superset_Admin": ["Admin"],
    "Superset_Alpha": ["Alpha"],
    "Superset_Gamma": ["Gamma"]
}
