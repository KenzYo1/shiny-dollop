# Program Microwave Pintar
# Simulasi microwave pintar

# KAMUS:
# t : int
# started : bool
# presets, foodlist : list[str]
# power_choice : list[float]
# timer_list : list[int]
# food_lists_info : list[[int, float]]
# on : int
# menu L int

# ALGORITMA:
t = 0
started = False

presets = ["Kembali", "Defrost", "Cook", "Reheat"]
food_lists = ["Kembali", "Kentang", "Popcorn", "Pizza", "Minuman", "Roti-rotian"]
food_lists_info = [[420, 1.0], [180, 1.0], [480, 0.4], [90, 1.0], [360, 0.5]]
power_choice = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
timer_list = [0, 15, 30, 45, 60]
power = power_choice[-1]
on = 0
menu = 0

print("=================================")
print("Welcome to shiny-dollop Microwave")
print("=================================")
nyala = input("Nyalakan microwave? (y/n) ")

if nyala == "y":
    on = 1
else:
    on = 0

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
    cek = 0

    while cek == 0:
        menu = int(input("Enter [1 - 5]: "))
        if 1 <= int(menu) <= 5:
            cek = 1
        else:
            print("Input harus [1 - 5]")

    match menu:
        case 1:
            print("\n\nTimer\n")
            cek = 0
            while cek == 0:
                timer = int(input("Input timer [15/30/45/60] (detik), [0] untuk set timer: "))
                if timer not in timer_list:
                    print("Input harus [15/30/45/60], [0] untuk set timer ")
                elif timer in timer_list and timer != 0 and t + timer <= 3600:
                    t += timer
                elif timer > 3600:
                    print("Timer kelamaan")
                    cek = 1
                elif timer == 0:
                    print(f"Timer set ke {t // 60:02d}:{t % 60:02d}")
                    cek = 1

        case 2:
            print("\n\nPower\n")
            cek = 0
            while cek == 0:
                power_input = int(input("Input power [10/20/30/40/50/60/70/80/90/100](%), [0] untuk keluar: "))
                if power_input / 100 in power_choice:
                    power = power_input / 100
                    cek = 1
                elif power_input == 0:
                    cek = 1
                else:
                    print("Input harus [10/20/30/40/50/60/70/80/90/100](%), [0] untuk keluar")

        case 3:
            print("\n\n\n\n\n")
            started = 1
            if (t == 0):
                print("Timer belum di set")
            elif (power == 0):
                print("Power belum di set")
            else:
                started = 1
                print("Microwave Dimulai!")
                while started and t > 0:
                    print(f"[{t // 60:02d}:{t % 60:02d}]")
                    t -= 1
                    if input("Input 'y' to stop") == "y":
                        started = 0
                        t = 0
                        power = 1.0
                print("tutututut timer habis")

                if input("Matikan microwave? (y/n) ") == "y":
                    print("terima kasih telah menggunakan shinny-dollop")
                    exit()
        case 4:
            lanjut = True
            while lanjut:
                t, power = 0, 1.0
                print("\n\n======== Presets ========:")
                [print(f"{i}. {presets[i]}") for i in range(len(presets))]
                us_input = int(input("\n"))
                if us_input == 0:
                    lanjut = False
                if us_input == 1:
                    print("Defrost : Durasi 10 Menit per 0,5 Kg Daging, Max 3 Kg")
                    meat = int(input("Berat daging yang ingin dipanaskan? "))
                    if meat > 3:
                        print("Terlalu berat")
                    if meat <= 0:
                        print("Berat yang tidak mungkin")
                    elif 0 < meat <= 3:
                        t = meat * 20 * 60
                        power = 0.2
                        print(f"Timer: {t//60:02d}:{t%60:02d}", f"\nPower: {power:.0%}")
                        confirm = input("Konfirmasi? (y/n) ")
                        if confirm == "y":
                            lanjut = False
                        else:
                            lanjut = True

                if us_input == 2 and lanjut == True:
                    print("Berikut adalah list makanan yang bisa dimasak:")
                    [print(f"{i}. {food_lists[i]}") for i in range(len(food_lists))]
                    makanan = int(input("Silakan pilih opsi makanan yang akan dimasak [0 - 5] "))
                    if makanan == 0:
                        lanjut = True
                    if 1 <= makanan <= 5:
                        food = food_lists[makanan]
                        t = food_lists_info[makanan-1][0]
                        power = food_lists_info[makanan-1][1]
                        print(f"Makanan yang dimasak adalah {food}",
                              f"\nTimer: {t//60:02d}:{t%60:02d}", f"\nPower: {power:.0%}")
                        confirm = input("Konfirmasi? (y/n) ")
                        if confirm == "y":
                            lanjut = False
                        else:
                            lanjut = True
                    else:
                        print("Input hanya dari [0 - 5]")

                if us_input == 3 and lanjut == True:
                    t = 60
                    power = 1.0
                    print(f"Timer: {t//60:02d}:{t%60:02d}", f"\nPower: {power:.0%}")
                    confirm = input("Konfirmasi? (y/n) ")
                    if confirm == "y":
                        lanjut = False
                    else:
                        lanjut = True
                elif us_input > 3 or us_input < 0:
                    print("Input hanya dari [0 - 3]")
        case 5:
            print("terima kasih telah menggunakan shinny-dollop")
            exit()
