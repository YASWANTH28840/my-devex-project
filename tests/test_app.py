"""Unit tests for the Flask application."""

import json
from unittest.mock import MagicMock, patch

import pytest

from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestHealthCheck:
    """Tests for the health check endpoint."""

    def test_home_endpoint_returns_200(self, client):
        """Test that / endpoint returns 200 OK."""
        response = client.get("/")
        assert response.status_code == 200

    def test_home_endpoint_returns_correct_json(self, client):
        """Test that / endpoint returns correct JSON structure."""
        response = client.get("/")
        data = json.loads(response.data)

        assert data["service"] == "devex-sample"
        assert data["status"] == "ok"

    def test_home_endpoint_content_type(self, client):
        """Test that / endpoint returns JSON content type."""
        response = client.get("/")
        assert response.content_type == "application/json"


class TestProductsEndpoint:
    """Tests for the /products endpoint."""

    @patch("app.requests.get")
    def test_products_endpoint_returns_200(self, mock_get, client):
        """Test that /products endpoint returns 200 when external API succeeds."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"products": []}
        mock_get.return_value = mock_response

        response = client.get("/products")
        assert response.status_code == 200

    @patch("app.requests.get")
    def test_products_endpoint_returns_api_data(self, mock_get, client):
        """Test that /products endpoint returns data from external API."""
        expected_data = {"products": [{"id": 1, "name": "Test Product"}]}
        mock_response = MagicMock()
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        response = client.get("/products")
        data = json.loads(response.data)

        assert data == expected_data

    @patch("app.requests.get")
    def test_products_endpoint_handles_timeout(self, mock_get, client):
        """Test that /products endpoint handles timeout errors gracefully."""
        import requests

        mock_get.side_effect = requests.Timeout("Connection timeout")

        response = client.get("/products")
        assert response.status_code == 502
        data = json.loads(response.data)
        assert "error" in data

    @patch("app.requests.get")
    def test_products_endpoint_handles_http_error(self, mock_get, client):
        """Test that /products endpoint handles HTTP errors."""
        import requests

        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("HTTP Error")
        mock_get.return_value = mock_response

        response = client.get("/products")
        assert response.status_code == 502
        data = json.loads(response.data)
        assert data["error"] == "Failed to fetch products"

    @patch("app.requests.get")
    def test_products_endpoint_calls_correct_url(self, mock_get, client):
        """Test that /products endpoint calls the correct external API."""
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        client.get("/products")

        mock_get.assert_called_once_with("https://dummyjson.com/products", timeout=10)

    def test_products_endpoint_content_type(self, client):
        """Test that /products endpoint returns JSON content type."""
        with patch("app.requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.json.return_value = {}
            mock_get.return_value = mock_response

            response = client.get("/products")
            assert response.content_type == "application/json"


class TestErrorHandling:
    """Tests for error handling."""

    @patch("app.requests.get")
    def test_connection_error_returns_502(self, mock_get, client):
        """Test that connection errors return 502 status."""
        import requests

        mock_get.side_effect = requests.ConnectionError("Connection refused")

        response = client.get("/products")
        assert response.status_code == 502

    @patch("app.requests.get")
    def test_error_response_has_error_field(self, mock_get, client):
        """Test that error responses include error field."""
        import requests

        mock_get.side_effect = requests.RequestException("Generic error")

        response = client.get("/products")
        data = json.loads(response.data)
        assert "error" in data
        assert "details" in data
