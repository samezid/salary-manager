# manager/calculator.py

class Calculator:
    def calculate(self, salary, ratio):
        """
        Menghitung pembagian salary berdasarkan rasio.
        :param salary: float, gaji bulanan
        :param ratio: list[int], contoh: [50, 30, 20]
        :return: dict berisi nilai persen dan jumlah uang per kategori
        """
        needs = salary * ratio[0] / 100
        wants = salary * ratio[1] / 100
        savings = salary * ratio[2] / 100

        return {
            "persen": ratio,
            "jumlah": [needs, wants, savings]
        }
