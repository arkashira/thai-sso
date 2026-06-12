import datetime
from src.auth import AuthService, AuditLog, User

class AuditLogger:
    """
    Helper that records arbitrary events to the AuthService's audit log.
    The user information is passed as a plain dict; we convert it to a User
    instance without exposing sensitive fields in the log representation.
    """
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    def log(self, event: str, user: dict):
        """
        Record an event.

        Parameters
        ----------
        event: str
            Name of the event (e.g., "Authentication").
        user: dict
            Dictionary containing at least 'username' and optionally other fields.
            Sensitive fields like 'email' are ignored for the log representation.
        """
        # Build a User object but hide email in its __repr__
        user_obj = User(
            username=user.get("username", ""),
            email=user.get("email", ""),   # stored but not shown in repr
            consent=user.get("consent", False)
        )
        audit_log = AuditLog(datetime.datetime.now(), event, user_obj)
        self.auth_service.audit_logs[f"{user_obj.username}-{event}"] = audit_log
