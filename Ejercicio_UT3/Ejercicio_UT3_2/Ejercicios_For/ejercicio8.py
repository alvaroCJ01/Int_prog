coche1_pos=70
coche1_vel=1
coche2_pos=150
coche2_vel=-1

for _ in range(10000000000000000000000):
    coche1_pos=coche1_pos+coche1_vel
    coche2_pos=coche2_pos+coche2_vel
    if coche1_pos==coche2_pos:
        print(coche1_pos)
        quit()