'''Tipe Data Dictionary'''

import pandas

data_murid = {
    'nama' : 'Andi',
    'umur' : 20,
    'Asal' : 'Bandung'
}

#print(data_murid)

nama = ['Andi', 'Budi', 'Siska']
umur = [20, 19, 21]
asal = ['Bandung', 'Jakarta', 'Semarang']

data_murid = {
    'nama' : nama,
    'umur' : umur,
    'asal' : asal
}

print(data_murid)

print(pandas.DataFrame(data_murid))

