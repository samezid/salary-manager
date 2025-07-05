class UserInterface:
    def show_welcome(self):
        print("=" * 35)
        print(" SELAMAT DATANG DI SALARY MANAGER ")
        print("=" * 35)

    def get_salary_input(self):
        while True:
            try:
                user_input = input("\nMasukkan gaji bersih bulanan Anda (Rp): ").replace(",", "")
                salary = float(user_input)
                if salary <= 0:
                    print("Gaji harus lebih dari 0.")
                    continue
                return salary
            except ValueError:
                print("Input tidak valid. Masukkan angka tanpa huruf atau simbol lainnya.")

    def choose_ratio(self, ratios):
        print("\nPilih metode pembagian gaji:")
        for i, key in enumerate(ratios.keys(), 1):
            print(f"{i}. {key} ({ratios[key][0]}%/{ratios[key][1]}%/{ratios[key][2]}%)")

        while True:
            try:
                choice = int(input("Pilihan Anda [angka]: "))
                if 1 <= choice <= len(ratios):
                    name = list(ratios.keys())[choice - 1]
                    return name, ratios[name]
                else:
                    print("Pilihan tidak tersedia.")
            except ValueError:
                print("Input tidak valid. Masukkan angka.")

    def show_result(self, ratio_name, result):
        print("\n----------------------------------")
        print(f"Hasil Pembagian Gaji - {ratio_name}")
        print("----------------------------------")
        print(f"Needs   ({result['persen'][0]}%) : Rp {self._format_rupiah(result['jumlah'][0])}")
        print(f"Wants   ({result['persen'][1]}%) : Rp {self._format_rupiah(result['jumlah'][1])}")
        print(f"Savings ({result['persen'][2]}%) : Rp {self._format_rupiah(result['jumlah'][2])}")

    def ask_repeat(self):
        while True:
            ulang = input("\nIngin hitung ulang? (y/n): ").strip().lower()
            if ulang in ['y', 'n']:
                return ulang == 'y'
            else:
                print("Masukkan 'y' untuk ya, atau 'n' untuk tidak.")

    def show_exit_message(self):
        print("\nTerima kasih telah menggunakan Salary Manager!")

    def _format_rupiah(self, amount):
        return f"{amount:,.0f}".replace(",", ".")
