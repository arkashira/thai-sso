import datetime
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class User:
    username: str
    email: str = field(repr=False)   # hide email from __repr__
    consent: bool

@dataclass
class AuditLog:
    timestamp: datetime.datetime
    event: str
    user: User

class AuthService:
    def __init__(self):
        self.audit_logs: Dict[str, AuditLog] = {}

    def authenticate(self, username: str, password: str, consent: bool) -> User:
        """
        Simulate authentication. In a real system the password would be verified.
        An audit log entry is created for the authentication event.
        """
        user = User(username, "user@example.com", consent)
        key = f"{username}-auth"
        self.audit_logs[key] = AuditLog(datetime.datetime.now(), "Authentication", user)
        return user

    def get_audit_logs(self) -> Dict[str, AuditLog]:
        """Return the internal audit log dictionary."""
        return self.audit_logs
