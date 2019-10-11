from scipy.sparse import csr_matrix
import numpy as np

#IMPORTANT! Copy the names of the columns into the output file denseMatrixOutput1.data

if __name__ == "__main__":
	namefile = "denseMatrixOutput1.data"
	filas = 184  #Modifica estooo!  Linea 2 de archivoX.data
	cols = 249	#Modifica esto 		Linea 3 de archivoX.data	

	#f = open("abs.data", "r")  	# para leer offi absFormateado.data
	f2 = open (namefile, "w")     	# para escribir
	
	with open("abs.data") as f:
		line = f.readline()
		cnt = 1
		while (cnt<4):
			f2.write(line)
			cnt += 1
			line = f.readline()		
		while line and (cnt < filas+4):
			cnt += 1
			line = f.readline()
			x = line.split(";")
			f2.write(x[0]+";")		
			arr = [0.0] * (cols+1)
			for i in range(1,len(x)-1):
				pos = x[i].split(":")
				mynumber = int(pos[0])
				arr[mynumber] = pos[1]
				#print(mynumber)
			print("lin"+str(cnt))
			print("."+x[len(x)-1]+"ok")			
			arr[249] = float(x[len(x)-1])			
			#print(arr)
			#s = input()
			for i in range(0,len(arr)-1):
				f2.write(str(arr[i])+";")
			f2.write(str(arr[len(arr)-1]))
			f2.write('\n')
			#f2.write()
			#print( line.strip() )			
			
	f2.close()
#Remove the last line		
