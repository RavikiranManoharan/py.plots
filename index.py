import numpy as np
import matplotlib.pyplot as plt

#function declaration section

def plot(c,d):
	
	xlbl = input("Enter the X unit: ")
	xlbl = xlbl.upper()
	ylbl = input("Enter the Y unit: ")
	ylbl = ylbl.upper()
	plt.title("PN JD")
	plt.plot(c,d)
	plt.scatter(c,d)
	plt.xlabel(xlbl)
	plt.ylabel(ylbl)
	plt.xlim(0,20)
	plt.ylim(0,20)
	plt.show()


def static_forward_resistance(v,i):
	v=float(v)
	i=float(i)
	rlt=v/i
	print(f"Static forward resistance (Vf) = {rlt} ohm\n\n")
	


def static_reverse_resistance(v,i):
	v=float(v)
	i=float(i)
	rlt=v/i
	print(f"Static reverse resistance (Vf) = {rlt} ohm\n\n")	


def dynamic_forward_resistance(vdg,idg,vds,ids):
	vdg=float(vdg)
	vds=float(vds)
	idg=float(idg)
	ids=float(ids)
	
	
	delv = vdg-vds
	deli = idg-ids
	
	r = delv/deli
	
	print(f"Dynamic forward resistance (rf) = {r} ohm\n\n")
	


def dynamic_reverse_resistance(vdg,idg,vds,ids):
	vdg=float(vdg)
	vds=float(vds)
	idg=float(idg)
	ids=float(ids)
	
	
	delv = vdg-vds
	deli = idg-ids
	
	r = delv/deli
	
	print(f"Dynamic reverse resistance (rf) = {r} ohm\n\n")
	
	

#main program


print("\t\t------NOTE------\n")
print("number of value in X and Y axis should be same\n\n")

x = []
y = []

num = input("Enter the total number of elements in X axis: ")
num = int(num)

print("Enter the values of X axis: ")

for i in range(num):
	
	a=input()
	x.append(a)

print("Enter the values of Y axis: ")

for i in range(num):
	b=input()
	y.append(b)

print("----Static Forward Resistance----")
voltsf = input("Enter the value of forward voltage: ")
ampssf = input("Enter the value of forward current: ")
print("\n\n")


print("----Dynamic forward resistance----")
vfg = input("Enter the greater value of forward voltage: ")
vfs = input("Enter the smaller value of forward voltage: ")

afg = input("Enter the greater value of forward current: ")
afs = input("Enter the smaller value of forward current: ")
print("\n\n")


print("----Static Reverse Resistance----")
voltsr = input("Enter the value of reverse voltage: ")
ampssr = input("Enter the value of reverse current: ")
print("\n\n")

print("----Dynamic forward resistance----")
vrg = input("Enter the greater value of forward voltage: ")
vrs = input("Enter the smaller value of forward voltage: ")

arg = input("Enter the greater value of forward current: ")
ars = input("Enter the smaller value of forward current: ")
print("\n\n")


#calling functions

static_forward_resistance(voltsf,ampssf)

dynamic_forward_resistance(vfg,afg,vfs,afs)


static_forward_resistance(voltsr,ampssr)

dynamic_forward_resistance(vrg,arg,vrs,ars)

plot(x,y)

	
