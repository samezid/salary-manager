from manager.user_interface import UserInterface
from manager.ratio_loader import RatioLoader
from manager.calculator import Calculator

class SalaryManager:
    def __init__(self):
        self.ui = UserInterface()
        self.ratio_loader = RatioLoader()
        self.calculator = Calculator()

    def run(self):
        self.ui.show_welcome()
        ratios = self.ratio_loader.load_ratios()

        while True:
            gaji = self.ui.get_salary_input()
            name, ratio = self.ui.choose_ratio(ratios)
            hasil = self.calculator.calculate(gaji, ratio)
            self.ui.show_result(name, hasil)

            if not self.ui.ask_repeat():
                self.ui.show_exit_message()
                break