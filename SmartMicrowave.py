# Program Microwave Pintar
# Simulasi microwave pintar

# KAMUS:

# ALGORITMA:
t = 0
started = False
# temp = float(input("Suhu awal: "))
moisture_content = 0.9
# max_temp = float(input("suhu maksumum: "))
power_choice = [0.1,0.2,0.3, 0.4,0.5, 0.6,0.7, 0.8,0.9, 1.0]
power = 0
on = 0
print("=================================")
print("Welcome to shiny-dollop Microwave")
print("=================================")
nyala = input("Nyalakan microwave (y/n)")
if nyala == "y": on = 1
else: on = 0
while on:
    print(f"Waktu = {t} detik")
    print(f"power = {power} %")
    print("Menu : ")
    print("1. Set Timer")
    print("2. Set Power")
    print("3. Start Micromave")
    print("4. Exit")
    cek = 0
    while(cek == 0):
        menu = int(input("Enter [1 - 4]: "))
        if(menu > 0 and menu < 5):
            cek = 1
        else:
            print("Input must be [1 - 4]")
            menu = int(input(">> "))
    match menu:
        case 1:
            print("\n\nTimer\n")
            cek = 0
            while(cek == 0):
                timer = int(input("Input timer [0/15/30/45/60] (sekon): "))
                if(timer !=0 and timer != 15 and timer != 30 and timer != 45 and timer != 60):
                    print("Input must be [0/15/30/45/60]")
                    timer = int(input(">> "))
                else:
                    cek = 1
            # limit timernya
            if(t + timer < 3600):
                print(f"Timer set to {t}")  
                t += timer
            else:
                print("timer kelamaan")
                
        case 2:
            print("\n\nPower\n")
            cek = 0
            while(cek == 0):
                power_input = int(input("Input power [0/10/20/30/40/50/60/70/80/90/100](%): "))
                if(power_input / 10 <= len(power_choice) or power_input == 0):
                    cek = 1
                else:
                    print("Input must be [0/10/20/30/40/50/60/70/80/90/100]")
                    power_input = int(input(">> "))        
            power = power_input
            
        case 3:
            print("\n\n\n\n\n")
            started = 1
            if(t == 0):
                print("Timer belum di set")
            elif(power == 0):
                print("power belum di set")
            else:
                started = 1
                while(started and t >= 0):
                    menit = t//60
                    detik = t%60
                    t -= 1
                    print(f"[{menit}:{detik}]")
                    if input("Input 'y' to stop") == "y":
                        started = 0
                print("tutututut timer habis")
                if input("Matikan microwave? (y/n)") == "y":
                    print("terima kasih telah menggunakan shinny-dollop")
                    exit()
        case 4:
            print("terima kasih telah menggunakan shinny-dollop")
            exit()
                        
            
    # match input:
    #     case "15s":
    #         t += 15
    #     case "30s":
    #         t += 30
    #     case "45s":
    #         t += 45
    #     case "1m":
    #         t += 60
    #     case "power":
    #         power_choice = (power_choice+1) % len(power)
    #         if power_choice == 4:
    #             print("mode daya: maksimum")
    #         else:
    #             print("mode daya:", int(power[power_choice]*100),"%")
    #     case "start":
    #         started = True
    #     case "exit":

# while started and t > 0 and temp < max_temp:
#     print(str(t // 60)+":"+str(t % 60))
#     t -= 1
#     temp += power[power_choice]
#     if input("tekan stop? ") == "ya":
#         started = False

# if not started:
#     print("microwave dihentikan")
# elif t == 0:
#     print("selesai")
# elif temp >= max_temp:
#     print("suhu maksimum tercapai")

# ADD presets:
# Defrost, Warm, Cook, Food Presets, 