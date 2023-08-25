import unittest
import time
from github import Github
import os
from unittest.mock import patch, Mock

from src import repo_creator

class TestRepoIntegration(unittest.TestCase):
    
    def setUp(self):
        self.token = os.getenv('YOUR_GITHUB_PERSONAL_ACCESS_TOKEN')
        if not self.token:
            raise ValueError("GitHub token not found in environment")
        self.github = Github(self.token)
        self.user = self.github.get_user()
        self.test_repo_name = "test_repo_" + str(int(time.time()))  # Unique name to avoid conflicts

    def test_create_and_delete_repo(self):
        # Ensure the repo doesn't exist at first
        with self.assertRaises(Exception):
            repo = self.user.get_repo(self.test_repo_name)

        # Create the repository
        repo = self.user.create_repo(self.test_repo_name, private=True)

        # Verify that it now exists
        repo = self.user.get_repo(self.test_repo_name)
        self.assertEqual(repo.name, self.test_repo_name)

        # Now clean up: delete the test repository
        repo.delete()

        # Ensure it's deleted
        with self.assertRaises(Exception):
            repo = self.user.get_repo(self.test_repo_name)



if __name__ == "__main__":
    unittest.main()
