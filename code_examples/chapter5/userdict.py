from collections import UserDict

def get_nutrition_information(text):
    return "arugula"

def get_aliases(text):
    if text == 'rocket':
        return ['arugula']
class NutritionalInformation(UserDict):
    def __getitem__(self, key):
        try:
            return self.data[key]
        except KeyError:
            pass
        for alias in get_aliases(key):
            try:
                return self.data[alias]
            except KeyError:
                pass
        raise KeyError(f"Could not find {key} or any of its aliases")

nutrition = NutritionalInformation()
nutrition["arugula"] = get_nutrition_information("arugula")
assert nutrition["arugula"] == nutrition["rocket"] # arugula == rocket
assert nutrition.get("rocket", "No Key Found") == nutrition['arugula']
