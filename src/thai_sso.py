import json
import hashlib
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional

@dataclass
class User:
    user_id: str
    username: str
    email: str
    consent_given: bool
    password: str  # Store the hashed password

@dataclass
class AuditLog:
    timestamp: str
    user_id: str
    action: str
    status: str
    details: Dict

class ThaiSSO:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.audit_logs: List[AuditLog] = []
        self.consent_required = True

    def register_user(self, user_id: str, username: str, email: str, password: str) -> bool:
        if user_id in self.users:
            return False
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[user_id] = User(user_id, username, email, False, hashed_password)
        self._log_audit("register", "success", {"user_id": user_id})
        return True

    def authenticate(self, user_id: str, password: str) -> bool:
        if user_id not in self.users:
            self._log_audit("authenticate", "failure", {"user_id": user_id, "reason": "user_not_found"})
            return False
        user = self.users[user_id]
        if not user.consent_given and self.consent_required:
            self._log_audit("authenticate", "failure", {"user_id": user_id, "reason": "consent_not_given"})
            return False
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password != user.password:
            self._log_audit("authenticate", "failure", {"user_id": user_id, "reason": "invalid_password"})
            return False
        self._log_audit("authenticate", "success", {"user_id": user_id})
        return True

    def give_consent(self, user_id: str) -> bool:
        if user_id not in self.users:
            return False
        self.users[user_id].consent_given = True
        self._log_audit("consent", "success", {"user_id": user_id})
        return True

    def _log_audit(self, action: str, status: str, details: Dict):
        log_entry = AuditLog(
            timestamp=datetime.now().isoformat(),
            user_id=details.get("user_id", "unknown"),
            action=action,
            status=status,
            details=details
        )
        self.audit_logs.append(log_entry)

    def get_audit_logs(self) -> List[AuditLog]:
        return self.audit_logs

    def save_state(self, file_path: str) -> bool:
        state = {
            "users": {uid: {"username": u.username, "email": u.email, "consent_given": u.consent_given, "password": u.password} for uid, u in self.users.items()},
            "audit_logs": [{"timestamp": log.timestamp, "user_id": log.user_id, "action": log.action, "status": log.status, "details": log.details} for log in self.audit_logs],
            "consent_required": self.consent_required
        }
        try:
            with open(file_path, 'w') as f:
                json.dump(state, f)
            return True
        except Exception:
            return False

    def load_state(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r') as f:
                state = json.load(f)
            self.users = {uid: User(uid, u["username"], u["email"], u["consent_given"], u["password"]) for uid, u in state["users"].items()}
            self.audit_logs = [AuditLog(log["timestamp"], log["user_id"], log["action"], log["status"], log["details"]) for log in state["audit_logs"]]
            self.consent_required = state["consent_required"]
            return True
        except Exception:
            return False
