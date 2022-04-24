import statistics

print("Tugas Algoritma dan Pemrogaman 1")

A = eval(input("A="))
B = eval(input("B="))
C = eval(input("C="))
D = eval(input("D="))
E = eval(input("E="))
data = (A, B, C, D, E)
ratarata = statistics.mean(data)

print("Hasil rata rata adalah = ",ratarata)
