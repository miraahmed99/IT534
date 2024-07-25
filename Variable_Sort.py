class VariableSort:
    """ Class to sort float, string, and integers
    """

    def __init__(self):
        """_Initialize the class
        """
        self.strings = []
        self.floats = []
        self.integers = []

    def add_variables(self, var):
        """Each variable is added based on the proper type

        Args:
            string, float, integer are all added

        Raises:
            ValueError: non alphabetic character
            TypeError: if variable is not allowed
        """
        if isinstance(var, str):
            if var.isalpha():
                self.strings.append(var)
            else:
                raise ValueError("Contains Non-Alphabetic characters")
        elif isinstance(var, float):
            self.floats.append(var)
        elif isinstance(var, int):
            self.integers.append(var)
        else:
            raise TypeError("Bad Type")
        
    def get_strings(self):
        """returns string

        Returns:
             list of strings
        """
        return self.strings
    
    def get_floats(self):
        """returns floats

        Returns:
             list of floats
        """
        return self.floats
    
    def get_integers(self):
        """returns integers

        Returns:
             list of integers
        """
        return self.integers