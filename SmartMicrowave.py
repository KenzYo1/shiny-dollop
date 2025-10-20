# Program Microwave Pintar
# Simulasi microwave pintar

# KAMUS:

# ALGORITMA:
t = 0
started = False
temp = float(input("Suhu awal: "))
moisture_content = 0.9
max_temp = float(input("suhu maksumum: "))
power = [0.2, 0.4, 0.6, 0.8, 1.0]
power_choice = 4
while not started:
    match input("tekan tombol: "):
        case "15s":
            t += 15
        case "30s":
            t += 30
        case "45s":
            t += 45
        case "1m":
            t += 60
        case "power":
            power_choice = (power_choice+1) % len(power)
            if power_choice == 4:
                print("mode daya: maksimum")
            else:
                print("mode daya:", int(power[power_choice]*100),"%")
        case "start":
            started = True

while started and t > 0 and temp < max_temp:
    print(str(t // 60)+":"+str(t % 60))
    t -= 1
    temp += power[power_choice]
    if input("tekan stop? ") == "ya":
        started = False

if not started:
    print("microwave dihentikan")
elif t == 0:
    print("selesai")
elif temp >= max_temp:
    print("suhu maksimum tercapai")

# ADD presets:
# Defrost, Warm, Cook, Food Presets, 