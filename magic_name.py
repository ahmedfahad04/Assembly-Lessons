name = input("Enter your name get the encription: ")

print("Result >>",end='')
for i in name:
	print(int(ord(i)),end='')

print(end="\n")

code = input("Enter the encription code of your name to get the real name: ")

print("Result >>",end='')
i=0
while(i < len(code)):

	if code[i] != '1':
		#print(">>" + code[i:i+2])
		print(chr(int(code[i:i+2])),end='')
		i = i+2
	else:
		#print(">>" + code[i:i+3])
		print(chr(int(code[i:i+3])),end='')
		i = i+3
	
print(end="\n")
