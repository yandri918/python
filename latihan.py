print("hello world")
a = 7
b = 3
c = a+b
print(c)
age = 23
salary = "1500000"
print(type(age))
print(type(salary))
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))
x = True
print(type(x))
b = "dicoding.com"
print(type(b))
print(b[2])
print(b[2:])
nama = "andriyanto"
print(f"hello nama saya {nama}")
print ("nama saya {}".format(nama))
print("nama saya %s"%(nama))
a =[1,2,"belajar"]
print(type(a))
print(a[2])
a[0]= "kemarin"
print (a)
d= (1, "andriyanto",2)
print(type(d))
print(d[0:2])
print(d[2])
e={1,2,3,4,5,6,7}
print(type(e))
print(e)
set1= {1,2,4,5,7,8,6}
set2={5,6,7,9,}
union = set1.union(set2)
print("union:",union)
intersection=set1.intersection(set2)
print("intersection:",intersection)
z= {'nama':'andriyanto','umur':35,'status':'menikah','pekerjaan':'petani'}
print(type(z))

print(z['status'])
z['hobi']= 'programming'
print(z)
z ['nama']='rina'
print(z)
print(float(12))
print(int(2.3))
print(set([1,2,3]))
print(tuple({1,3,5}))
print(list('andriyanto'))
print(dict[[1,2],[3,4]])
print(dict([(2,3),(3.4,3)]))
print(type(z))
kata = 'dicoding'
kata = kata.upper()
print(kata)
tulisan = 'DICODING'
tulisan = tulisan.lower()
print(tulisan)
print(' '.join(['dicoding','indonesia','menyala']))
print('menyala indonesiaku'.split())
kata ='dicoding'
print(kata.islower())
print('dicoding'.center(10,'_'))
contoh_list =[1,2,3,4,1,2,4]
print(contoh_list)
print(len(contoh_list))
contoh_data=set([1,2,2,3,4,4,5,6])
print(contoh_data)
print(len(contoh_data))
data="belajar python"
print(data)
print(len(data))
angka =[12,23,3445,23,332,456]
print(min(angka))
print(max(angka))
genap =[2,4,6,8,8,8,4,4,6,4,4,4,4,4,4,4,44]
print(genap.count(4))
string ="sekarang adalah waktunya untuk belajar bahasa pemrograman"
substring= "y"
print(string.count(substring))
print('belajar'in string)
print('saat'not in string)
data= ['kaos','merah','small']
jenis,warna,ukuran=data
print(data)
print(jenis)
print(warna)
print(ukuran)
kendaraan =['motor','becak','helikopter','pesawat']
kendaraan.sort()
print(kendaraan)