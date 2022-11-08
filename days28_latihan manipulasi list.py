#program manupulasi list

number = int(input("masukkan angka:"))

angka = [a for a in range ( 1, number+1)]
print (angka)

#jumlah elemen pada list
print (65*"=")
print ("jumlah elemen pada list")

jumlah_elemen = len(angka)
print ("jumlah elemen",jumlah_elemen)

# hasil penjumlahan elemen - elemen pada list
print (65*"=")
jumlah = sum(angka)
print ("hasil penjumlahan list",jumlah)

# item terakhir pada list
print (65*"=")

last_angka = angka [-1]
print ("elemen terakhir pada list",last_angka)

# urutan terbalik pada list
print (65*"=")
angka.reverse()
print ("urutan angka terbalik",angka)


# jika list mengandung nilai 7 maka print yes dan jika tidak mengandung nilai 7 maka print no
print (65*"=")

if number >= 7 :
    print ("yes, angka list yang anda masukkan mengandung angka 7")
elif number <= 7:
    print ("no, list yang anda masukkan tidak mengandung angka 7 ")
    




