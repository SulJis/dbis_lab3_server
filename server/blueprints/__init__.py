from server.blueprints.auth import auth as auth_blueprint
from server.blueprints.create import create as create_blueprint
from server.blueprints.read import read as read_blueprint
from server.blueprints.update import update as update_blueprint
from server.blueprints.delete import delete as delete_blueprint

__all__ = ["auth_blueprint", "create_blueprint", "read_blueprint", "update_blueprint", "delete_blueprint"]
