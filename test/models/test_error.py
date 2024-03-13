import unittest
from src.testsdk.models.Error import Error


class TestErrorModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_error(self):
        # Create Error class instance
        test_model = Error(message="ullam", code=5)
        self.assertEqual(test_model.message, "ullam")
        self.assertEqual(test_model.code, 5)

    def test_error_required_fields_missing(self):
        # Assert Error class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Error()


if __name__ == "__main__":
    unittest.main()
