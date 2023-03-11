import time
print("Viper")
print("Made by LoganPaxton")
print("Loading Resources")
time.sleep(5)
print("Resources loaded sucsessfully!")
print("WARNING! FEATURES MAY NOT WORK AS INTENDED!")
time.sleep(1)

detection = False

malicious = ("rd c:\system32", "del c:\,", ",rd c:\,")

filename = input("File >> ")
fs = open(filename, 'r')
batch = fs.read()
fs.close()
codes = batch.split("\n")
for line in codes:
   for maliciouscode in malicious:
       if maliciouscode.lower() == line.lower():
           detection = True
if detection == True:
    print("Virus detected!")
