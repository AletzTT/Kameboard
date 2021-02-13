from functools import wraps
from flask import abort
from flask_login import current_user
from coreapp.admin.models import Project
from coreapp.auth.models import User


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(current_user, 'is_admin', False)
        if not is_admin:
            abort(401)
        return f(*args, **kws)
    return decorated_function

def owner_required(f):
    @wraps(f)
    def wrapper(*args, **kws):
        project_id = kws['project_id']
        project = Project.get_by_id(project_id)
        if project is None:
            abort(404)
        user = User.get_by_id(current_user.id)
        if project.author is not user:
            abort(401)
        return f(*args, **kws)
    return wrapper

            