from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Desserts")
        self.assertEqual(str(self.category), "Desserts")

    def test_category_iter(self):
        recipe1 = Recipe.objects.create(
            title="Cake", description="Desc", instructions="Inst", 
            ingredients="Ingr", category=self.category
        )
        recipe2 = Recipe.objects.create(
            title="Pie", description="Desc", instructions="Inst", 
            ingredients="Ingr", category=self.category
        )
        
        # Тестуємо метод __iter__
        recipes_in_category = list(self.category)
        self.assertEqual(len(recipes_in_category), 2)
        self.assertIn(recipe1, recipes_in_category)
        self.assertIn(recipe2, recipes_in_category)

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Main Course")
        self.recipe = Recipe.objects.create(
            title="Steak",
            description="Juicy steak",
            instructions="Grill it.",
            ingredients="Meat, Salt",
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Steak")
        self.assertEqual(self.recipe.category.name, "Main Course")
        self.assertTrue(self.recipe.created_at)
        self.assertTrue(self.recipe.updated_at)