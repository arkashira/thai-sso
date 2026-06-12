import pytest
from src.auth import AuthService, User
from src.audit_logger import AuditLogger

def test_audit_logger():
    auth_service = AuthService()
    audit_logger = AuditLogger(auth_service)
    user = User("test_user", "user@example.com", True)
    audit_logger.log("Authentication", {"username": user.username, "email": user.email, "consent": user.consent})
    audit_logs = auth_service.get_audit_logs()
    assert len(audit_logs) == 1
    assert list(audit_logs.keys())[0] == "test_user-Authentication"
