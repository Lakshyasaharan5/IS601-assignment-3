class Operations:

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their sum (a + b).
        """
        return a + b 

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their difference (a - b).        
        """
        return a - b 

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their product (a * b).        
        """
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        This static method takes two numbers (a and b) and returns their quotient (a / b).        
        Raises error if divided by zero
        """
        if b == 0:            
            raise ValueError("Can't divide by zero.")
        return a / b  

