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
t = 0
started = False

presets = ["Kembali", "Defrost", "Cook", "Reheat"]
food_lists = ["Kembali", "Kentang", "Popcorn", "Pizza", "Minuman", "Roti-rotian"]
food_lists_info = [[420, 1.0], [180, 1.0], [480, 0.4], [90, 1.0], [360, 0.5]]
power_choice = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
timer_list = [0, 15, 30, 45, 60]
power = power_choice[-1]
on = True
menu = 0

print("=================================")
print("Welcome to shiny-dollop Microwave")
print("=================================")

if input("Nyalakan microwave? (y/n) ") == "y":
    on = True
else:
    on = False

while on:
    print("====================")
    print(f"Waktu = {t} detik")
    print(f"power = {power:.0%}")
    print("Menu : ")
    print("1. Set Timer")
    print("2. Set Power")
    print("3. Start Microwave")
    print("4. Presets")
    print("5. Exit")
    print("====================")
    cek = False

    while not cek:
        menu = int(input("Enter [1 - 5]: "))
        if 1 <= int(menu) <= 5:
            cek = True
        else:
            print("Input harus [1 - 5]")

    match menu:
        case 1:
            print("\n\nTimer\n")
            cek = False
            while not cek:
                timer = int(input("Input timer [15/30/45/60] (detik), [0] untuk balik: "))
                if timer not in timer_list:
                    print("Input harus [15/30/45/60], [0] untuk set timer ")
                elif timer in timer_list and timer != 0 and t + timer <= 3600:
                    t += timer
                    print(f"Timer set ke {t // 60:02d}:{t % 60:02d}")
                elif t + timer > 3600:
                    print("Timer kelamaan")
                elif timer == 0:
                    cek = True

        case 2:
            print("\n\nPower\n")
            cek = False
            while not cek:
                power_input = int(input("Input power [10/20/30/40/50/60/70/80/90/100](%), [0] untuk keluar: "))
                if power_input / 100 in power_choice:
                    power = power_input / 100
                    cek = True
                elif power_input == 0:
                    cek = True
                else:
                    print("Input harus [10/20/30/40/50/60/70/80/90/100](%), [0] untuk keluar")

        case 3:
            print("\n\n\n\n\n")
            if (t == 0):
                print("Timer belum di set")
            elif (power == 0):
                print("Power belum di set")
            else:
                started = True
                print("Microwave Dimulai!")
                while started and t > 0:
                    print(f"[{t // 60:02d}:{t % 60:02d}]")
                    t -= 1
                    if input("Input 'y' to stop") == "y":
                        started = False
                        t = 0
                        power = 1.0
                if started:
                    print("tutututut timer habis")
                else:
                    print("microwave dihentikan")

                if input("Matikan microwave? (y/n) ") == "y":
                    print("terima kasih telah menggunakan shinny-dollop")
                    on = False
        case 4:
            lanjut = True
            while lanjut:
                print("\n\n======== Presets ========:")
                [print(f"{i}. {presets[i]}") for i in range(len(presets))]
                us_input = int(input("\n"))
                match us_input:
                    case 0:
                        lanjut = False
                    case 1:
                        print("Defrost : Durasi 10 Menit per 0,5 Kg Daging, Max 3 Kg")
                        meat = int(input("Berat daging yang ingin dipanaskan? "))
                        if meat > 3:
                            print("Terlalu berat")
                        if meat <= 0:
                            print("Berat yang tidak mungkin")
                        elif 0 < meat <= 3:
                            temporary_t = meat * 20 * 60
                            temporary_power = 0.2
                            print(f"Timer: {temporary_t//60:02d}:{temporary_t%60:02d}", f"\nPower: {temporary_power:.0%}")
                            confirm = input("Konfirmasi? (y/n) ")
                            if confirm == "y":
                                t = temporary_t
                                power = temporary_power
                                lanjut = False

                    case 2:
                        print("Berikut adalah list makanan yang bisa dimasak:")
                        [print(f"{i}. {food_lists[i]}") for i in range(len(food_lists))]
                        makanan = int(input("Silakan pilih opsi makanan yang akan dimasak [0 - 5] "))
                        if makanan == 0:
                            lanjut = True
                        if 1 <= makanan <= 5:
                            food = food_lists[makanan]
                            temporary_t = food_lists_info[makanan-1][0]
                            temporary_power = food_lists_info[makanan-1][1]
                            print(f"Makanan yang dimasak adalah {food}",
                                f"\nTimer: {temporary_t//60:02d}:{temporary_t%60:02d}", f"\nPower: {temporary_power:.0%}")
                            confirm = input("Konfirmasi? (y/n) ")
                            if confirm == "y":
                                t = temporary_t
                                power = temporary_power
                                lanjut = False
                        else:
                            print("Input hanya dari [0 - 5]")

                    case 3:
                        temporary_t = 60
                        temporary_power = 1.0
                        print(f"Timer: {temporary_t//60:02d}:{temporary_t%60:02d}", f"\nPower: {temporary_power:.0%}")
                        confirm = input("Konfirmasi? (y/n) ")
                        if confirm == "y":
                            t = temporary_t
                            power = temporary_power
                            lanjut = False
                    case _:
                        print("Input hanya dari [0 - 3]")
        case 5:
            print("terima kasih telah menggunakan shinny-dollop")
            on = False
