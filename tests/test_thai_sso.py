import pytest
from thai_sso import ThaiSSO, User, AuditLog

def test_register_user():
    sso = ThaiSSO()
    assert sso.register_user("user1", "testuser", "test@example.com", "password123")
    assert not sso.register_user("user1", "testuser", "test@example.com", "password123")  # Duplicate registration

def test_authenticate_without_consent():
    sso = ThaiSSO()
    sso.register_user("user1", "testuser", "test@example.com", "password123")
    assert not sso.authenticate("user1", "password123")

def test_authenticate_with_consent():
    sso = ThaiSSO()
    sso.register_user("user1", "testuser", "test@example.com", "password123")
    sso.give_consent("user1")
    assert sso.authenticate("user1", "password123")

def test_audit_logs():
    sso = ThaiSSO()
    sso.register_user("user1", "testuser", "test@example.com", "password123")
    sso.give_consent("user1")
    sso.authenticate("user1", "password123")
    logs = sso.get_audit_logs()
    assert len(logs) == 3  # register, consent, authenticate
    assert logs[0].action == "register"
    assert logs[1].action == "consent"
    assert logs[2].action == "authenticate"

def test_data_minimization():
    sso = ThaiSSO()
    sso.register_user("user1", "testuser", "test@example.com", "password123")
    user = sso.users["user1"]
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert isinstance(user.consent_given, bool)

def test_save_and_load_state():
    sso = ThaiSSO()
    sso.register_user("user1", "testuser", "test@example.com", "password123")
    sso.give_consent("user1")
    sso.authenticate("user1", "password123")
    assert sso.save_state("test_state.json")
    new_sso = ThaiSSO()
    assert new_sso.load_state("test_state.json")
    assert len(new_sso.get_audit_logs()) == 3
