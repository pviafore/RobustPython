def get_nutrition_information(text):
    return "arugula"

def get_aliases(text):
    if text == 'rocket':
        return ['arugula']

class NutritionalInformation(dict):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            pass
        for alias in get_aliases(key):
            try:
                return super().__getitem__(alias)
            except KeyError:
                pass
        raise KeyError(f"Could not find {key} or any of its aliases")

nutrition = NutritionalInformation()
nutrition["arugula"] = get_nutrition_information("arugula")
assert nutrition["arugula"] == nutrition["rocket"] # arugula == rocket
assert nutrition.get("rocket", "No Key Found") == "No Key Found" # Uh Oh
