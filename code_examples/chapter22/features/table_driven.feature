Feature: Vegan-friendly menu

Scenario Outline: Vegan Substitutions
  Given an order containing <dish_name>,
  When I ask for vegan substitutions
  Then <result>

 Examples: Vegan Substitutable
   | dish_name                   | result |
   | a Cheeseburger with Fries   | I receive the meal with no animal products   |
   | Cobb Salad                  | I receive the meal with no animal products   |
   | French Fries                | I receive the meal with no animal products   |
   | Lemonade                    | I receive the meal with no animal products   |

 Examples: Not Vegan Substitutable
   | dish_name     | result |
   | Meatloaf      | a non-vegan-substitutable error shows up |
   | Meatballs     | a non-vegan-substitutable error shows up |
   | Fried Shrimp  | a non-vegan-substitutable error shows up |
