# -*- coding: utf-8 -*-
"""
Session management for the Thai‑SSO service.

* `sessions` – a global in‑memory map ``session_id -> Session``.
* All accesses are protected by ``_sessions_lock`` (a re‑entrant lock) so the
  structure is safe under concurrent web‑request threads and background jobs.
"""

from __future__ import annotations

import threading
from typing import Dict

# ----------------------------------------------------------------------
# Global store & lock
# ----------------------------------------------------------------------
sessions: Dict[str, "Session"] = {}          # session_id -> Session
_sessions_lock = threading.RLock()          # exported in __init__.py

# ----------------------------------------------------------------------
# Helper (can be replaced by a proper logger later)
# ----------------------------------------------------------------------
def _log_logout(user_id: str, session_id: str) -> None:
    """Simple stdout logging – keep it side‑effect‑free for tests."""
    print(f"User {user_id} logged out from session {session_id}")

# ----------------------------------------------------------------------
# Public API
# ----------------------------------------------------------------------
def logout(user_id: str) -> None:
    """
    Invalidate **all** sessions that belong to ``user_id``.

    The function is safe to call from any thread because it holds
    ``_sessions_lock`` for the whole read‑modify‑write cycle.

    Steps:
    1. Build a list of session IDs that match the user.
    2. Pop each entry from ``sessions`` (pop returns the Session object).
    3. Log the logout using the popped object – no stale dictionary look‑ups.
    """
    # 1️⃣ Gather IDs under lo
