from view import *
from PyQt6.QtWidgets import *
import operator
import math


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Initializes the controller, adding the logic necessary for the calculator
        """
        # PyQt vars from Test 10
        super().__init__()
        self.setupUi(self)

        # Basic variables for calculator functionality, with current_num determining
        # which number of a two-number calculation the user is on, num1 and num2 holding
        # number values, operator determining which math operator is active, clear_entry
        # determining whether clear button clears all or just the current number,
        # add_decimal preparing to add a decimal, and ans_displayed allowing text from an
        # answer to be overwritten by the next number press
        self.current_num = 1
        self.num1 = 0
        self.num2 = None
        self.operator = None
        self.clear_entry = False
        self.add_decimal = False
        self.ans_displayed = False


        # Functions
        #self.button_clear.clicked.connect(lambda: self.clear())
        self.button_plus.clicked.connect(lambda: self.addition())
        self.button_minus.clicked.connect(lambda: self.subtraction())
        self.button_times.clicked.connect(lambda: self.multiplication())
        self.button_divide.clicked.connect(lambda: self.division())
        self.SUBMIT.clicked.connect(lambda: self.clear())
        self.button_sin.clicked.connect(lambda: self.sine())
        self.button_cos.clicked.connect(lambda: self.cosine())
        self.button_tan.clicked.connect(lambda: self.tangent())

    


    def get_and_validate_nontrig(self) -> tuple:
        """
        Helper function that obtains the two numbers from the input fields and stores them
        """
        num1 = self.entry1.text().strip()
        num2 = self.entry2.text().strip()


        print(num1)

        try:
            num1 = float(num1)
            num2 = float(num2)
        except:
            self.outputLabel.setText("Enter two numbers!")
            return 

        return num1, num2



    def get_and_validate_trig(self) -> tuple:
        """
        Helper function that obtains the two numbers from the input fields and stores them
        """
        num1 = self.entry1.text().strip()




        try:
            num1 = float(num1)
        except:
            self.outputLabel.setText("Enter two numbers!")
            return

        return num1


    def addition(self) -> None:
        """
        Sets operator to addition and performs retroactive calculations if pending.
        """
        if self.get_and_validate_nontrig() is None:
            return

        num1, num2 = self.get_and_validate_nontrig()

        self.outputLabel.setText(f"The sum is\n {num1+num2}")



    def subtraction(self) -> None:
        """
        Sets operator to addition and performs retroactive calculations if pending.
        """
        if self.get_and_validate_nontrig() is None:
            return

        num1, num2 = self.get_and_validate_nontrig()

        self.outputLabel.setText(f"The difference is\n {num1-num2}")
  


    def multiplication(self) -> None:
        """
        Sets operator to multiplication and performs retroactive calculations if pending.
        """
        if self.get_and_validate_nontrig() is None:
            return

        
        num1, num2 = self.get_and_validate_nontrig()

        self.outputLabel.setText(f"The product is\n {num1*num2}")


    def division(self) -> None:
        """
        Sets operator to division and performs retroactive calculations if pending.
        """
        if self.get_and_validate_nontrig() is None:
            return


        num1, num2 = self.get_and_validate_nontrig()

        if num2 == 0:
            self.outputLabel.setText(f"Cannot divide by 0")
            return
        self.outputLabel.setText(f"The quotient is\n {num1/num2:.4f}")


    def clear(self) -> None:
        """
        Returns result of calculations to entry label, making that number the new num1
        for future calculations and ensuring it can be easily overwritten with number's
        block for if ans_displayed
        """
        
        self.entry1.setText("")
        self.entry2.setText("")
        self.outputLabel.setText("")


    def sine(self) -> None:
        """
        Calculates and immediately displays the sine of the current number, with
        display logic very similar to that of return method.
        """
        if self.get_and_validate_trig() is None:
            return

        num1 = self.get_and_validate_trig()
        self.outputLabel.setText(f"The sine of the first number is \n{math.sin(num1):.4f}")

    def cosine(self) -> None:
        """
        Calculates and immediately displays the cosine of the current number, with
        display logic very similar to that of return method.
        """
        if self.get_and_validate_trig() is None:
            return
  

        
        num1 = self.get_and_validate_trig()
        self.outputLabel.setText(f"The cosine of the first number is \n{math.cos(num1):.4f}")


    def tangent(self) -> None:
        """
        Calculates and immediately displays the tangent of the current number, with
        display logic very similar to that of return method.
        """
        if self.get_and_validate_trig() is None:
            return


        
        num1 = self.get_and_validate_trig()
        try:
            self.outputLabel.setText(f"The tangent of the first number is\n {math.sin(num1):.4f}")
        except:
            self.outputLabel.setText("The tangent of the first number\n does not exist")


