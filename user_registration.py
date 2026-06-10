def test_pdpa_compliant_account():
    # Arrange
    user_data = create_pdpa_compliant_user_data()
    user_account = create_user_account(user_data)

    # Act
    is_pdpa_compliant = is_pdpa_compliant_account(user_account)

    # Assert
    assert is_pdpa_compliant == True

def test_encrypted_user_data_at_rest():
    # Arrange
    user_data = create_pdpa_compliant_user_data()
    encrypted_user_data = encrypt_user_data(user_data)
    decrypted_user_data = decrypt_user_data(encrypted_user_data)

    # Act & Assert
    assert decrypted_user_data == user_data

def test_encrypted_user_data_in_transit():
    # Arrange
    user_data = create_pdpa_compliant_user_data()
    encrypted_user_data = encrypt_user_data(user_data)
    network_traffic = capture_network_traffic(encrypted_user_data)
    decrypted_user_data = decrypt_network_traffic(network_traffic)

    # Act & Assert
    assert decrypted_user_data == user_data

def test_user_can_delete_account_and_data():
    # Arrange
    user_data = create_pdpa_compliant_user_data()
    user_account = create_user_account(user_data)

    # Act
    delete_user_account(user_account)
    deleted_user_data = get_deleted_user_data(user_account.user_id)

    # Assert
    assert deleted_user_data is None

def test_accessible_and_compliant_privacy_policy():
    # Arrange
    privacy_policy_url = get_privacy_policy_url()

    # Act & Assert
    scraped_privacy_policy = scrape_webpage(privacy_policy_url)
    is_compliant = is_privacy_policy_compliant(scraped_privacy_policy)
    assert is_compliant == True