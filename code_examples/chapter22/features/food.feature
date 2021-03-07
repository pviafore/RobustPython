Feature: Vegan-friendly menu

Scenario: Can substitute for vegan alternatives
Given an order containing a Cheeseburger with Fries
When I ask for vegan substitutions
Then I receive the meal with no animal products
