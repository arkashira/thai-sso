import pytest
from src.auth import AuthService, User

def test_authenticate():
    auth_service = AuthService()
    user = auth_service.authenticate("test_user", "test_password", True)
    assert user.username == "test_user"
    assert user.email == "user@example.com"
    assert user.consent == True

def test_audit_logs():
    auth_service = AuthService()
    user = auth_service.authenticate("test_user", "test_password", True)
    audit_logs = auth_service.get_audit_logs()
    assert len(audit_logs) == 1
    assert list(audit_logs.keys())[0] == "test_user-auth"

def test_data_minimization():
    auth_service = AuthService()
    user = auth_service.authenticate("test_user", "test_password", True)
    audit_logs = auth_service.get_audit_logs()
    # The string representation of the AuditLog should not contain the email address
    assert "email" not in str(audit_logs[list(audit_logs.keys())[0]])
