ip=' 192.168.001.010 '
ip=ip.strip()
ip2=ip[::-1]
b=ip.count('.')
c=ip.find('.')
d=ip2.find('.')
print(ip[:c])
e=ip2[:d]
print(e[::-1])