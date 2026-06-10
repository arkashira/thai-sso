def test_login_success_returns_token(mocker):
    mock_db = mocker.patch('user_login.db')
    mock_db.verify_credentials.return_value = True
    mock_db.create_session.return_value = 'signed-token-123'
    resp = user_login.login(username='user', password='pass')
    assert resp.status_code == 200
    assert resp.json()['token'] == 'signed-token-123'
    mock_db.log_login.assert_called_once()  # PDPA audit

def test_login_failure_generic_error(mocker):
    mock_db = mocker.patch('user_login.db')
    mock_db.verify_credentials.return_value = False
    resp = user_login.login(username='unknown', password='wrong')
    assert resp.status_code == 401
    assert resp.json()['error'] == 'Invalid credentials'
    # Ensure no user‑specific info leaked
    assert 'unknown' not in resp.text

def test_login_pdpa_data_minimization(mocker):
    mock_db = mocker.patch('user_login.db')
    mock_db.verify_credentials.return_value = True
    mock_db.create_session.return_value = 'tok'
    user_login.login(username='user', password='pass')
    # Verify only allowed fields are stored
    stored = mock_db.create_session.call_args[0][0]
    assert set(stored.keys()) == {'user_id', 'login_ts', 'session_hash'}

def test_logout_invalidates_token(mocker):
    mock_db = mocker.patch('user_login.db')
    mock_db.invalidate_session.return_value = True
    resp = user_login.logout(token='signed-token-123')
    assert resp.status_code == 200
    mock_db.invalidate_session.assert_called_once_with('signed-token-123')