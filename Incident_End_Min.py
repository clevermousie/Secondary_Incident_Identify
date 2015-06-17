input_file = open("./../incident_period.txt","r")
output_file = open("./../log/incident_end.txt","w")
dom = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for line in input_file.readlines():
	temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9,temp10,temp11 = [int(x) for x in line.split()]
	doy=0
	for i in range(temp6):
		doy+=dom[i]
	doy+=temp7-1
	moy = doy*60*24+60*temp9+temp10
	print >> output_file,moy
input_file.close()
output_file.close()
