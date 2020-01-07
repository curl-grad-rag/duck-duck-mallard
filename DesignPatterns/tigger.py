class tigger:
    """
    Tigger Class -- Non-Singleton pattern
    """
    def __str__(self):
        return "I'm the only one!"
    
    def roar(self):
        return "Grrrrrrrr!"

class _tigger2:
    """
    Tigger Class -- Singleton pattern
    """
    def __str__(self):
        return "I'm the only one!"
    
    def roar(self):
        return "Grrrrrrrr!"

_instance = None
def tigger2():
    """
    Function that makes Tigger2 Singleton
    """
    # Insert lock if multi-threading
    global _instance
    if _instance == None:
        _instance = _tigger2()
    return _instance