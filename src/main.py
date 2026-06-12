import argparse
import json
from src.auth import AuthService
from src.audit_logger import AuditLogger

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", type=str, required=True)
    parser.add_argument("--password", type=str, required=True)
    parser.add_argument("--consent", action="store_true")
    args = parser.parse_args()

    auth_service = AuthService()
    audit_logger = AuditLogger(auth_service)

    # Authenticate the user (creates an audit entry)
    user = auth_service.authenticate(args.username, args.password, args.consent)

    # Log an explicit authentication event using the logger (demonstrates data minimization)
    audit_logger.log(
        "Authentication",
        {"username": user.username, "email": user.email, "consent": user.consent},
    )

    # Serialize audit logs – we convert each AuditLog to a dict for JSON friendliness
    def serialize_audit(log):
        return {
            "timestamp": log.timestamp.isoformat(),
            "event": log.event,
            "user": {
                "username": log.user.username,
                # email intentionally omitted to respect minimization
                "consent": log.user.consent,
            },
        }

    serialized = {k: serialize_audit(v) for k, v in auth_service.get_audit_logs().items()}
    print(json.dumps(serialized, indent=4))

if __name__ == "__main__":
    main()
