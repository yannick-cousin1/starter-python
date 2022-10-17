
txt = input("Entrez un texte : ")

with open("./output.txt", "a") as file:
	file.write(txt)
	file.write('\n')
with open("./output.txt") as file:
	print (file.read())

