import unittest
from unittest.mock import patch, Mock

from src.repo_creator import git_commands

class TestInvalidToken(unittest.TestCase):

    @patch('src.repo_creator.Github')
    @patch('src.repo_creator.os.chdir')
    @patch('src.repo_creator.subprocess.Popen')
    def test_invalid_token(self, MockPopen, MockChdir, MockGithub):
        MockGithub.side_effect = Exception("Bad credentials")
        MockPopen.return_value = Mock()  # This prevents actual subprocess calls.
        
        with self.assertRaises(Exception) as context:
            git_commands("dummy_path", "dummy_commit", True, use_ssh=True)
            
        self.assertIn("Bad credentials", str(context.exception))
