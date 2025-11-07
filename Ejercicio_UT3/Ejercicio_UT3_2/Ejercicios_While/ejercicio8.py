coche1_pos=70
coche1_vel=1
coche2_pos=150
coche2_vel=-1

while coche1_pos < coche2_pos:
    coche1_pos=coche1_pos+coche1_vel
    coche2_pos=coche2_pos+coche2_vel

print(f"Los coches se encontrarán en el KM: {coche1_pos}")