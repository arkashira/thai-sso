def logout(session_id):
    global sessions
    if session_id in sessions:
        del sessions[session_id]
        # Invalidate all other sessions for the user
        for sid, session in sessions.items():
            if session.user.id == sessions[session_id].user.id:
                del sessions[sid]