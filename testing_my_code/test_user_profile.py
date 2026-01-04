import pytest # type: ignore
import os
from user_profile import UserProfile

@pytest.fixture
def user():
    """Create a user profile, then delete the file after test."""
    # SETUP: Create user
    profile = UserProfile("ahad", "test_profile.txt")

    yield profile  # Give to test

    # TEARDOWN: Delete the file after test
    if os.path.exists("test_profile.txt"):
        os.remove("test_profile.txt")

def test_set_preference(user):
    """Test setting preferences."""
    user.set_preference("theme", "dark")
    assert user.get_preference("theme") == "dark"

def test_save_and_load(user):
    """Test saving and loading profile."""
    user.set_preference("theme", "dark")
    user.set_preference("language", "en")

    user.save()  # Saves to file

    # Create NEW user and load
    new_user = UserProfile("ahad", "test_profile.txt")
    new_user.load()

    assert new_user.get_preference("theme") == "dark"
    assert new_user.get_preference("language") == "en"
