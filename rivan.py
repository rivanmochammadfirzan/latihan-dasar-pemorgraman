from logging.handlers import BaseRotatingHandler
from opcode import HAVE_ARGUMENT


nama = input("nama barang = ")
harga = int(input("price = "))
rumus = ((harga/100) * 10) + 10
rumus2 = ((harga/100))
print ("harga jual", nama ,"=", rumus, "\n", "keuntungan = ", rumus2)
 



