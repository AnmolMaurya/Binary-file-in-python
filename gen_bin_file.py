import struct

file = open('bin_file','wb')
id = 0
val = id

for i in range(50):
	entry = struct.pack('<HL',id,val)
	id+=1
	val = id
	file.write(entry)
	file.flush()

file.close()
