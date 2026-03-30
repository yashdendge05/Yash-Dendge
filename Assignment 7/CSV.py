import csv
#Write to CSV File
f=open("Students.csv","w",newline="")
write = csv.writer(f)
write.writerow(["Name","Marks"])
write.writerow(["Amit","85"])
write.writerow(["Riya","90"])
f.close()

#Read From Csv File
f=open("Students.csv","r")
reader = csv.reader(f)

for row in reader:
    print(row)
f.close()