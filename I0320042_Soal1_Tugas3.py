print("===Daftar Nama===")
Nama_teman = ['Hana', 'Angela', 'Aratia', 'Candrika', 'Divana', 'Gea', 'Ayu', 'Adrian', 'Ervizal', 'Stefany']
print(Nama_teman)
#Menampilkan list index
print("Isi index ke [4] adalah", Nama_teman[4])
print("Isi index ke [6] adalah", Nama_teman[6])
print("Isi index ke [7] adalah", Nama_teman[7])
#Mengganti Nama Teman
Nama_teman[3] = 'Rara'
Nama_teman[5] = 'Sasa'
Nama_teman[9] = 'Audrey'
#Menambah Nama Teman
Nama_teman.append('Alifiana')
Nama_teman.append('Deadila')
#Menampilkan Perulangan Nama Teman
f = 0
for j in range(0,12):
    print(Nama_teman[f])
    f = f+1
print(len(Nama_teman))


    

