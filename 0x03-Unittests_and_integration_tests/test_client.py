#!/usr/bin/env python3
"""Module for testing the GithubOrgClient class."""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """Class to test the functionality of GithubOrgClient."""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        based on the organization name.
        """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns the expected result
        based on the mocked payload.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "World"}
            mock_org.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that public_repos returns the expected list of repos.
        Check that both the mocked property and get_json are called once.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_url:
            mock_public_url.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
            expected_repos = [repo["name"] for repo in json_payload]
            self.assertEqual(result, expected_repos)
            mock_public_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that has_license correctly determines if a repo
        has a specified license key.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class for integration testing with fixtures."""

    @classmethod
    def setUpClass(cls):
        """
        Set up patching for requests.get to provide fixture payloads
        for the integration tests.
        """
        config = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    def test_public_repos(self):
        """
        Integration test for public_repos ensuring repos returned
        match the expected repos in the payload.
        """
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """
        Integration test for public_repos with a specified license
        filtering for repos matching the license key.
        """
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock_get.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get after tests complete."""
        cls.get_patcher.stop()