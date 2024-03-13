import unittest
import responses
from src.testsdk.net.http_client import HTTPClient
from http_exceptions import ClientException
from src.testsdk.services.pets import Pets


class TestPets_(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    @responses.activate
    def test_list_pets(self):
        # Mock the API response
        responses.get("http://petstore.swagger.io/v1/pets", json={}, status=200)
        # call the method to test
        test_service = Pets("testkey")
        response = test_service.list_pets(7)
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_list_pets_error_on_non_200(self):
        # Mock the API response
        responses.get("http://petstore.swagger.io/v1/pets", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Pets("testkey")
            test_service.list_pets(9)
        responses.reset()

    @responses.activate
    def test_create_pets(self):
        # Mock the API response
        responses.post("http://petstore.swagger.io/v1/pets", json={}, status=200)
        # call the method to test
        test_service = Pets("testkey")
        response = test_service.create_pets({})
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_create_pets_error_on_non_200(self):
        # Mock the API response
        responses.post("http://petstore.swagger.io/v1/pets", json={}, status=404)
        with self.assertRaises(ClientException):
            test_service = Pets("testkey")
            test_service.create_pets({})
        responses.reset()

    @responses.activate
    def test_show_pet_by_id(self):
        # Mock the API response
        responses.get(
            "http://petstore.swagger.io/v1/pets/9119642480", json={}, status=200
        )
        # call the method to test
        test_service = Pets("testkey")
        response = test_service.show_pet_by_id("9119642480")
        self.assertEqual(response, {})
        responses.reset(),

    @responses.activate
    def test_show_pet_by_id_required_fields_missing(self):
        # Mock the API response
        responses.get(
            "http://petstore.swagger.io/v1/pets/9607272303", json={}, status=202
        )
        with self.assertRaises(TypeError):
            test_service = Pets("testkey")
            test_service.show_pet_by_id()
        responses.reset(),

    @responses.activate
    def test_show_pet_by_id_error_on_non_200(self):
        # Mock the API response
        responses.get(
            "http://petstore.swagger.io/v1/pets/7933233347", json={}, status=404
        )
        with self.assertRaises(ClientException):
            test_service = Pets("testkey")
            test_service.show_pet_by_id("7933233347")
        responses.reset()


if __name__ == "__main__":
    unittest.main()
