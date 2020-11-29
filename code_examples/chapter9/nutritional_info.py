from dataclasses import dataclass
@dataclass(eq=True)
class NutritionInformation: #type: ignore
    calories: int
    fat: int
    carbohydrates: int

nutritionals = [NutritionInformation(calories=100, fat=1, carbohydrates=3),
                NutritionInformation(calories=50, fat=6, carbohydrates=4),
                NutritionInformation(calories=125, fat=12, carbohydrates=3)]

try:
    sorted(nutritionals) # type: ignore
    assert False
except TypeError as e:
    pass


@dataclass(eq=True, order=True)
class NutritionInformation: # type: ignore
    calories: int
    fat: int
    carbohydrates: int

nutritionals = [NutritionInformation(calories=100, fat=1, carbohydrates=3),
                NutritionInformation(calories=50, fat=6, carbohydrates=4),
                NutritionInformation(calories=125, fat=12, carbohydrates=3)]

assert sorted(nutritionals) == [NutritionInformation(calories=50, fat=6, carbohydrates=4), # type: ignore
                                NutritionInformation(calories=100, fat=1, carbohydrates=3),
                                NutritionInformation(calories=125, fat=12, carbohydrates=3)] 


@dataclass(eq=True)
class NutritionInformation: # type: ignore
    calories: int
    fat: int
    carbohydrates: int

    def __lt__(self, rhs) -> bool:
        return ((self.fat, self.carbohydrates, self.calories) < 
                (rhs.fat, rhs.carbohydrates, rhs.calories))

    def __le__(self, rhs) -> bool:
        return self < rhs or self == rhs

    def __gt__(self, rhs) -> bool:
        return not self <= rhs

    def __ge__(self, rhs) -> bool:
        return not self < rhs

nutritionals = [NutritionInformation(calories=100, fat=1, carbohydrates=3),
                NutritionInformation(calories=50, fat=6, carbohydrates=4),
                NutritionInformation(calories=125, fat=12, carbohydrates=3)]
assert sorted(nutritionals) ==[NutritionInformation(calories=100, fat=1, carbohydrates=3), NutritionInformation(calories=50, fat=6, carbohydrates=4), NutritionInformation(calories=125, fat=12, carbohydrates=3)] # type: ignore
