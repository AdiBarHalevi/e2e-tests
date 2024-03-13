import unittest
from src.testsdk.models.Pet import Pet


class TestPetModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_pet(self):
        # Create Pet class instance
        test_model = Pet(name="hic", id=2, tag="velit")
        self.assertEqual(test_model.name, "hic")
        self.assertEqual(test_model.id, 2)
        self.assertEqual(test_model.tag, "velit")

    def test_pet_required_fields_missing(self):
        # Assert Pet class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = Pet()


if __name__ == "__main__":
    unittest.main()
