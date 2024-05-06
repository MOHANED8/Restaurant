bash
$ python main.py



### Listing the Menu
bash
$ curl http://localhost:8080/listMeals


JSON output:
bash

[{"id": 4, "name": "Beef stir-fry with rice", "ingredients": [{"name": "Beef", "quantity": 115, "quantity_type": "gram"}, {"name": "Rice", "quantity": 120, "quantity_type": "gram"}, {"name": "Vegetables", "quantity": 240, "quantity_type": "gram"}]}, {"id": 9, "name": "Fruit salad with mixed berries and yogurt", "ingredients": [{"name": "Mixed berries", "quantity": 240, "quantity_type": "gram"}, {"name": "Yogurt", "quantity": 120, "quantity_type": "millilitre"}]}, {"id": 3, "name": "Grilled chicken with roasted vegetables", "ingredients": [{"name": "Chicken", "quantity": 85, "quantity_type": "gram"}, {"name": "Vegetables", "quantity": 240, "quantity_type": "gram"}]}, {"id": 6, "name": "Grilled salmon with roasted asparagus", "ingredients": [{"name": "Salmon", "quantity": 85, "quantity_type": "gram"}, {"name": "Asparagus", "quantity": 240, "quantity_type": "gram"}]}, {"id": 2, "name": "Pasta with marinara sauce and vegetables", "ingredients": [{"name": "Pasta", "quantity": 115, "quantity_type": "gram"}, {"name": "Marinara sauce", "quantity": 120, "quantity_type": "millilitre"}, {"name": "Vegetables", "quantity": 240, "quantity_type": "gram"}]}, {"id": 5, "name": "Pork chops with mashed potatoes and gravy", "ingredients": [{"name": "Pork chops", "quantity": 115, "quantity_type": "gram"}, {"name": "Mashed potatoes", "quantity": 120, "quantity_type": "gram"}, {"name": "Gravy", "quantity": 120, "quantity_type": "millilitre"}]}, {"id": 1, "name": "Rice and chicken bowl", "ingredients": [{"name": "Rice", "quantity": 120, "quantity_type": "gram"}, {"name": "Chicken", "quantity": 85, "quantity_type": "gram"}]}, {"id": 7, "name": "Shrimp scampi with linguine", "ingredients": [{"name": "Shrimp", "quantity": 115, "quantity_type": "gram"}, {"name": "Linguine", "quantity": 115, "quantity_type": "gram"}, {"name": "Butter", "quantity": 10, "quantity_type": "millilitre"}, {"name": "Garlic", "quantity": 10, "quantity_type": "gram"}, {"name": "White wine", "quantity": 60, "quantity_type": "millilitre"}]}, {"id": 8, "name": "Vegetarian stir-fry with tofu", "ingredients": [{"name": "Tofu", "quantity": 115, "quantity_type": "gram"}, {"name": "Rice", "quantity": 120, "quantity_type": "gram"}, {"name": "Vegetables", "quantity": 240, "quantity_type": "gram"}]}]


### Getting an Item from Menu
bash
$ curl http://localhost:8080/getMeal?id=2

JSON output:

bash
{"id": 2, "name": "Pasta with marinara sauce and vegetables", "ingredients": [{"name": "Pasta", "quantity": 115, "quantity_type": "gram"}, {"name": "Marinara sauce", "quantity": 120, "quantity_type": "millilitre"}, {"name": "Vegetables", "quantity": 240, "quantity_type": "gram"}]} 


### Quality Calculation With Ingredient Qualities

bash
$ curl -d "meal_id=3&garlic=high" -X POST http://localhost:8080/quality


JSON output:

bash
{"quality": 9.0}


### Price Calculation With Ingredient Qualities

bash
$ curl -d "meal_id=3&garlic=low" -X POST http://localhost:8080/price


JSON output:

bash
{ none}


### I'm Feeling Lucky

bash
$ curl -d "budget=42.42" -X POST http://localhost:8080/random


JSON response:

bash
{"error": "Not found"}


## Bonus Endpoints
### Searching For a Meal

bash
$ curl http://localhost:8080/search?query=beer


Example JSON output:

bash
  {"error": "Not found"}


### Finding the Highest Quality Meal For Given Budget

bash
$ curl -d "budget=42.42&is_vegetarian=false&is_vegan=false" -X POST http://localhost:8080/findHighest


JSON output:

bash
{"error": "Not found"}


### Finding the Highest Quality Version of a Meal For Given Budget

bash
$ curl -d "budget=42.42&meal_id=2&is_vegan=false" -X POST http://localhost:8080/findHighestOfMeal


JSON output:

bash
{"error": "Not found"}


## Dataset
### Dataset Content

<details>
  <summary>Expand to view the full dataset file</summary>

json
{
  "meals": [
    {
      "id": 1,
      "name": "Rice and chicken bowl",
      "ingredients": [
        { "name": "Rice", "quantity": 120, "quantity_type": "gram" },
        { "name": "Chicken", "quantity": 85, "quantity_type": "gram" }
      ]
    },
    {
      "id": 2,
      "name": "Pasta with marinara sauce and vegetables",
      "ingredients": [
        { "name": "Pasta", "quantity": 115, "quantity_type": "gram" },
        {
          "name": "Marinara sauce",
          "quantity": 120,
          "quantity_type": "millilitre"
        },
        { "name": "Vegetables", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 3,
      "name": "Grilled chicken with roasted vegetables",
      "ingredients": [
        { "name": "Chicken", "quantity": 85, "quantity_type": "gram" },
        { "name": "Vegetables", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 4,
      "name": "Beef stir-fry with rice",
      "ingredients": [
        { "name": "Beef", "quantity": 115, "quantity_type": "gram" },
        { "name": "Rice", "quantity": 120, "quantity_type": "gram" },
        { "name": "Vegetables", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 5,
      "name": "Pork chops with mashed potatoes and gravy",
      "ingredients": [
        { "name": "Pork chops", "quantity": 115, "quantity_type": "gram" },
        {
          "name": "Mashed potatoes",
          "quantity": 120,
          "quantity_type": "gram"
        },
        { "name": "Gravy", "quantity": 120, "quantity_type": "millilitre" }
      ]
    },
    {
      "id": 6,
      "name": "Grilled salmon with roasted asparagus",
      "ingredients": [
        { "name": "Salmon", "quantity": 85, "quantity_type": "gram" },
        { "name": "Asparagus", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 7,
      "name": "Shrimp scampi with linguine",
      "ingredients": [
        { "name": "Shrimp", "quantity": 115, "quantity_type": "gram" },
        { "name": "Linguine", "quantity": 115, "quantity_type": "gram" },
        { "name": "Butter", "quantity": 10, "quantity_type": "millilitre" },
        { "name": "Garlic", "quantity": 10, "quantity_type": "gram" },
        { "name": "White wine", "quantity": 60, "quantity_type": "millilitre" }
      ]
    },
    {
      "id": 8,
      "name": "Vegetarian stir-fry with tofu",
      "ingredients": [
        { "name": "Tofu", "quantity": 115, "quantity_type": "gram" },
        { "name": "Rice", "quantity": 120, "quantity_type": "gram" },
        { "name": "Vegetables", "quantity": 240, "quantity_type": "gram" }
      ]
    },
    {
      "id": 9,
      "name": "Fruit salad with mixed berries and yogurt",
      "ingredients": [
        { "name": "Mixed berries", "quantity": 240, "quantity_type": "gram" },
        { "name": "Yogurt", "quantity": 120, "quantity_type": "millilitre" }
      ]
    }
  ],

  "ingredients": [
    {
      "name": "Rice",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Long grain white rice",
          "quality": "high",
          "price": 3,
          "per_amount": "kilogram"
        },
        {
          "name": "Medium grain brown rice",
          "quality": "medium",
          "price": 2,
          "per_amount": "kilogram"
        },
        {
          "name": "Quick cooking white rice",
          "quality": "low",
          "price": 1.5,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Pasta",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "Semolina pasta",
          "quality": "high",
          "price": 2,
          "per_amount": "kilogram"
        },
        {
          "name": "Whole wheat pasta",
          "quality": "medium",
          "price": 1.5,
          "per_amount": "kilogram"
        },
        {
          "name": "Enriched pasta",
          "quality": "low",
          "price": 1,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Chicken",
      "groups": [],
      "options": [
        {
          "name": "Organic, free-range chicken",
          "quality": "high",
          "price": 10,
          "per_amount": "kilogram"
        },
        {
          "name": "Conventional chicken",
          "quality": "medium",
          "price": 7,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen chicken",
          "quality": "low",
          "price": 4,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Beef",
      "groups": [],
      "options": [
        {
          "name": "Grass-fed beef",
          "quality": "high",
          "price": 16,
          "per_amount": "kilogram"
        },
        {
          "name": "Grain-fed beef",
          "quality": "medium",
          "price": 12,
          "per_amount": "kilogram"
        },
        {
          "name": "Processed beef",
          "quality": "low",
          "price": 8,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Pork",
      "groups": [],
      "options": [
        {
          "name": "Heritage breed pork",
          "quality": "high",
          "price": 12,
          "per_amount": "kilogram"
        },
        {
          "name": "Conventional pork",
          "quality": "medium",
          "price": 9,
          "per_amount": "kilogram"
        },
        {
          "name": "Processed pork",
          "quality": "low",
          "price": 6,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Salmon",
      "groups": [],
      "options": [
        {
          "name": "Wild-caught salmon",
          "quality": "high",
          "price": 24,
          "per_amount": "kilogram"
        },
        {
          "name": "Farmed salmon",
          "quality": "medium",
          "price": 16,
          "per_amount": "kilogram"
        },
        {
          "name": "Canned tuna",
          "quality": "low",
          "price": 8,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Shrimp",
      "groups": [],
      "options": [
        {
          "name": "Wild-caught shrimp",
          "quality": "high",
          "price": 20,
          "per_amount": "kilogram"
        },
        {
          "name": "Farm-raised shrimp",
          "quality": "medium",
          "price": 15,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen shrimp",
          "quality": "low",
          "price": 10,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Vegetables",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic vegetables",
          "quality": "high",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional vegetables",
          "quality": "medium",
          "price": 5,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen vegetables",
          "quality": "low",
          "price": 3,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Fruit",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic fruit",
          "quality": "high",
          "price": 6,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional fruit",
          "quality": "medium",
          "price": 4,
          "per_amount": "kilogram"
        },
        {
          "name": "Canned fruit",
          "quality": "low",
          "price": 2,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Dairy",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "Organic, grass-fed dairy",
          "quality": "high",
          "price": 16,
          "per_amount": "litre"
        },
        {
          "name": "Conventional dairy",
          "quality": "medium",
          "price": 8,
          "per_amount": "litre"
        },
        {
          "name": "Processed dairy",
          "quality": "low",
          "price": 4,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Marinara sauce",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Homemade marinara sauce",
          "quality": "high",
          "price": 20,
          "per_amount": "litre"
        },
        {
          "name": "Store-bought marinara sauce",
          "quality": "medium",
          "price": 12,
          "per_amount": "litre"
        },
        {
          "name": "Canned marinara sauce",
          "quality": "low",
          "price": 6,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Butter",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "Grass-fed butter",
          "quality": "high",
          "price": 12,
          "per_amount": "kilogram"
        },
        {
          "name": "Conventional butter",
          "quality": "medium",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Margarine",
          "quality": "low",
          "price": 4,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Garlic",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic garlic",
          "quality": "high",
          "price": 6,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional garlic",
          "quality": "medium",
          "price": 4,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen garlic",
          "quality": "low",
          "price": 2,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "White wine",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "High-end white wine",
          "quality": "high",
          "price": 40,
          "per_amount": "litre"
        },
        {
          "name": "Mid-range white wine",
          "quality": "medium",
          "price": 30,
          "per_amount": "litre"
        },
        {
          "name": "Cheap white wine",
          "quality": "low",
          "price": 20,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Mashed potatoes",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Homemade mashed potatoes",
          "quality": "high",
          "price": 10,
          "per_amount": "litre"
        },
        {
          "name": "Store-bought mashed potatoes",
          "quality": "medium",
          "price": 7,
          "per_amount": "litre"
        },
        {
          "name": "Instant mashed potatoes",
          "quality": "low",
          "price": 4,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Gravy",
      "groups": [],
      "options": [
        {
          "name": "Homemade gravy",
          "quality": "high",
          "price": 10,
          "per_amount": "litre"
        },
        {
          "name": "Store-bought gravy",
          "quality": "medium",
          "price": 7,
          "per_amount": "litre"
        },
        {
          "name": "Instant gravy",
          "quality": "low",
          "price": 4,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Asparagus",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic asparagus",
          "quality": "high",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional asparagus",
          "quality": "medium",
          "price": 5,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen asparagus",
          "quality": "low",
          "price": 3,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Tofu",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "High-quality tofu",
          "quality": "high",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Medium-quality tofu",
          "quality": "medium",
          "price": 6,
          "per_amount": "kilogram"
        },
        {
          "name": "Low-quality tofu",
          "quality": "low",
          "price": 4,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Yogurt",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "Organic, grass-fed yogurt",
          "quality": "high",
          "price": 12,
          "per_amount": "litre"
        },
        {
          "name": "Conventional yogurt",
          "quality": "medium",
          "price": 8,
          "per_amount": "litre"
        },
        {
          "name": "Processed yogurt",
          "quality": "low",
          "price": 4,
          "per_amount": "litre"
        }
      ]
    },
    {
      "name": "Mixed berries",
      "groups": ["vegan", "vegetarian"],
      "options": [
        {
          "name": "Fresh, organic mixed berries",
          "quality": "high",
          "price": 12,
          "per_amount": "kilogram"
        },
        {
          "name": "Fresh, conventional mixed berries",
          "quality": "medium",
          "price": 8,
          "per_amount": "kilogram"
        },
        {
          "name": "Frozen mixed berries",
          "quality": "low",
          "price": 4,
          "per_amount": "kilogram"
        }
      ]
    },
    {
      "name": "Linguine",
      "groups": ["vegetarian"],
      "options": [
        {
          "name": "High-end linguine",
          "quality": "high",
          "price": 2,
          "per_amount": "kilogram"
        },
        {
          "name": "Mid-range linguine",
          "quality": "medium",
          "price": 1.5,
          "per_amount": "kilogram"
        },
        {
          "name": "Cheap linguine",
          "quality": "low",
          "price": 1,
          "per_amount": "kilogram"
        }
      ]
    }
  ]
}


</details>
