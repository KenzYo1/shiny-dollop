# Program Microwave Pintar
# Simulasi microwave pintar

# KAMUS:
# t : int
# started : bool
# presets, foodlist : list[str]
# power_choice : list[float]
# timer_list : list[int]
# food_lists : list[str]
# food_lists_info : list[[int, float]]
# on : bool
# cek : bool
# power_input : int
# power : float
# menu : int
# timer : int
# us_input : int
# meat : int
# confirm: bool
# makanan : int
# temporary_t : int
# temporary_power : float

# ALGORITMA:
# inisiasi variable

t = 0  # durasi timer
started = False  # state microwave lagi proses atau tidak
presets = ["Kembali", "Defrost", "Cook", "Reheat"]  # list preset microwave
food_lists = ["Kembali", "Kentang", "Popcorn", "Pizza", "Minuman", "Roti-rotian"]  # list menu makanan di preset "cook"
food_lists_info = [[420, 1.0], [180, 1.0], [480, 0.4], [90, 1.0], [360, 0.5]]  # list untuk detail food_lists
power_choice = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  # list daftar power
timer_list = [0, 15, 30, 45, 60]  # daftar pilihan untuk tambahan timer
power = power_choice[-1]  # default power
on = True  # state microwave nyala atau mati
menu = 0  # menyimpan pilihan menu user

# mulai program
print("=================================")
print("Welcome to shiny-dollop Microwave")
print("=================================")

if input("Nyalakan microwave? (y/n) ") == "y":
    on = True
else:
    on = False

# Selama microwave 'on' (on == True), loop ini akan terus berjalan
while on:
    # tampilan status dan menu
    print("====================")
    print(f"Timer = {t} detik")
    print(f"Power = {power:.0%}")
    print("Menu : ")
    print("1. Set Timer")
    print("2. Set Power")
    print("3. Start Microwave")
    print("4. Presets")
    print("5. Exit")
    print("====================")

    # 'cek' digunakan sebagai flag untuk validasi input menu
    cek = False

    # loop untuk validasi input
    while not cek:
        menu = int(input("Enter [1 - 5]: "))
        if 1 <= int(menu) <= 5:
            cek = True  # Input valid, hentikan loop validasi
        else:
            print("Input harus [1 - 5]")

    # 'match case' berfungsi seperti 'switch' untuk menjalankan kode berdasarkan pilihan 'menu'
    match menu:
        case 1:  # SET TIMER
            print("\n\nTimer\n")
            cek = False  # validasi belum valid
            while not cek:
                # Display timer
                timer = int(input("Input tambah timer [15/30/45/60] (detik), [0] untuk balik: "))
                if timer not in timer_list:
                    print("Input harus [15/30/45/60], [0] untuk set timer ")
                elif timer in timer_list and timer != 0 and t + timer <= 3600:
                    t += timer  # Tambahkan waktu ke timer yang sudah ada
                    print(f"Timer set ke {t // 60:02d}:{t % 60:02d}")
                elif t + timer > 3600:
                    print("Timer kelamaan")
                elif timer == 0:
                    cek = True  # Keluar dari loop timer

        case 2:
            print("\n\nPower")
            cek = False  # validasi belum valid
            while not cek:
                print(f"\nPower = {power:.0%}")
                power_input = int(input("Input power [10/20/30/40/50/60/70/80/90/100](%), [0] untuk keluar: "))

                if power_input / 100 in power_choice:
                    power = power_input / 100  # Set power sesuai dengan input user
                    cek = True  # Keluar dari menu power
                elif power_input == 0:
                    cek = True  # Keluar dari menu power
                else:
                    print("\nInput harus [10/20/30/40/50/60/70/80/90/100] atau [0] untuk keluar")

        case 3:  # START MICROWAVE
            print("\n\n\n\n\n")
            # Cek apakah sudah setup timer dan power
            if t == 0:
                print("Timer belum di set\n\n")
            elif power == 0:
                print("Power belum di set")
            # Setup sudah dilakukan
            else:
                started = True  # Microwave jalan
                print("Microwave Dimulai!")

                # Loop untuk countdown timer
                while started and t > 0:
                    print(f"[{t // 60:02d}:{t % 60:02d}]")  # Tampilkan sisa waktu
                    t -= 1  # Kurangi waktu 1 detik

                    # Cek apakah pengguna ingin menghentikan microwave
                    if input("Input 'y' to stop") == "y":
                        # Reset setup microwave
                        started = False
                        t = 0
                        power = 1.0
                if started:
                    # Timer selesai
                    print("tutututut timer habis")
                else:
                    # Tombol stop ditekan
                    print("microwave dihentikan")

                # Setelah selesai, tawarkan untuk mematikan microwave
                if input("Matikan microwave? (y/n) ") == "y":
                    print("terima kasih telah menggunakan shinny-dollop")
                    on = False  # Menghentikan seluruh program
        case 4:  # PRESETS
            # Flag untuk loop preset
            lanjut = True
            while lanjut:
                print("\n\n======== Presets ========:")
                # Menampilkan menu preset
                [print(f"{i}. {presets[i]}") for i in range(len(presets))]
                us_input = int(input("\n"))
                match us_input:
                    # Opsi 0: kembali ke menu utama
                    case 0:
                        lanjut = False
                    # Opsi 1: Defrost
                    case 1:
                        print("Defrost : Durasi 10 Menit per 0,5 Kg Daging, Max 3 Kg")
                        meat = int(input("Berat daging yang ingin dipanaskan? "))
                        if meat > 3:
                            print("\nTerlalu berat")
                        if meat <= 0:
                            print("\nBerat yang tidak mungkin")
                        elif 0 < meat <= 3:
                            temporary_t = meat * 20 * 60  # Hitung waktu (berat * 20 menit)
                            temporary_power = 0.2  # Set power ke 20%
                            # Menampilkan setup
                            print(f"Timer: {temporary_t // 60:02d}:{temporary_t % 60:02d}",
                                  f"\nPower: {temporary_power:.0%}")
                            confirm = input("Konfirmasi? (y/n) ")
                            if confirm == "y":
                                t = temporary_t
                                power = temporary_power
                                lanjut = False  # Konfirmasi, keluar loop preset

                    # Opsi 2: Cook
                    case 2:
                        print("Berikut adalah list makanan yang bisa dimasak:")
                        # Menampilkan opsi makanan
                        [print(f"{i}. {food_lists[i]}") for i in range(len(food_lists))]
                        makanan = int(input("Silakan pilih opsi makanan yang akan dimasak [0 - 5] "))
                        if makanan == 0:
                            lanjut = True  # Kembali ke menu preset
                        if 1 <= makanan <= 5:
                            # Mengambil data dari list yang sudah di inisiasi
                            food = food_lists[makanan]
                            temporary_t = food_lists_info[makanan - 1][0]
                            temporary_power = food_lists_info[makanan - 1][1]
                            # Menampilkan setup
                            print(f"Makanan yang dimasak adalah {food}",
                                  f"\nTimer: {temporary_t // 60:02d}:{temporary_t % 60:02d}",
                                  f"\nPower: {temporary_power:.0%}")
                            confirm = input("Konfirmasi? (y/n) ")
                            if confirm == "y":
                                t = temporary_t
                                power = temporary_power
                                lanjut = False
                        else:
                            print("\nInput hanya dari [0 - 5]")

                    # Opsi 3: Reheat
                    case 3:
                        temporary_t = 60  # Set waktu 60 detik
                        temporary_power = 1.0  # Set power 100%
                        # Menampilkan setup
                        print(f"Timer: {temporary_t // 60:02d}:{temporary_t % 60:02d}",
                              f"\nPower: {temporary_power:.0%}")
                        confirm = input("Konfirmasi? (y/n) ")
                        if confirm == "y":
                            t = temporary_t
                            power = temporary_power
                            lanjut = False  # Konfirmasi, keluar loop preset

                    # Validasi input untuk menu preset utama
                    case _:
                        print("Input hanya dari [0 - 3]")
        case 5:
            print("============================================")
            print("Terima kasih telah menggunakan shinny-dollop")
            print("============================================")
            on = False
