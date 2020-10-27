
class Bun:
    def __init__(self, args):
        pass

def are_buns_available():
    return False


def dispense_bun() -> Bun:
    if not are_buns_available():
        return None
    return Bun('Wheat')


assert dispense_bun() is None
