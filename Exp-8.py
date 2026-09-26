# Experiment 8
# Title: File Handling and I/O Reading/writing files

file = open(r"C:\Users\Asus\OneDrive\Desktop\PL Experiments\APP\input.txt", "r")
lines = file.readlines()
print("Number of lines:", len(lines))

first_two = lines[:2]
file.close()
file = open(r"C:\Users\Asus\OneDrive\Desktop\PL Experiments\APP\output.txt", "w")
file.writelines(first_two)

file.close()
print("First two lines written to output.txt")