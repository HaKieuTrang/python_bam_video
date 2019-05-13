import sys
import os
import hashlib
from Crypto.Hash import SHA256

block_size = 1024

file_name = "birthday.mp4"
file_size = os.path.getsize(file_name)

#kích thước khối cuối cùng
last_block_size = file_size % block_size

# số lượng khối 
number_of_blocks = file_size//block_size

print ("- File:", file_name, "\n- File size:", file_size, "\n- Last block size:", 
	last_block_size, "\n- Number of blocks:", number_of_blocks)

f = open(file_name, 'rb')

h = []
b = []
for i in range(0, number_of_blocks + 1):
	j = number_of_blocks - i
	f.seek(file_size - last_block_size - block_size*i)
	if(i == 0):
		b.append(f.read(last_block_size)) # đọc khối cuối cùng
		hash_object = hashlib.sha256(b[i]) 
		h.append(hash_object.digest()) # băm khối cuối cùng
	else:
		b.append(f.read(block_size)) # đọc các khối có kích thước 1024 bytes
		if (i == 1):
			h.append(b[1] + h[0]) # ghép khối gần cuối với giá trị băm của khối cuối cùng
			hash_object = hashlib.sha256(h[i]) 
			h[i] = (hash_object.digest()) 
		else:
			h.append(b[i] + h[i-1]) # ghép khối thứ n-1 với giá trị băm của khối n
			hash_object = hashlib.sha256(h[i]) 
			h[i] = (hash_object.digest()) 
			if (i == number_of_blocks):
				print("- Giá trị băm mã hóa cho video là: ")
				print (h[i].hex())