
txt = input("Entrez un texte : ")

with open("./output.txt", "a") as file: #open the file "output.txt" in "append mode"
	file.write(txt)						#append value of "txt" (user's input) in the file
	file.write('\n')					#line break

with open("./output.txt") as file:		#As we're using "with", the file closed automatically, so we need to open it
	print (file.read())					#again to read it (read mode by default)
										#It closes automatically again.
