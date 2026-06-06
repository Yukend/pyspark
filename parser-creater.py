f = open("/home/ubuntu/Downloads/magic-git/procedure.txt").readlines()
count = 1
v = 13
index = 10
pre = "duplicate_patient_"
for line in f:
    i = line.lower().replace("/", "_").replace(" ", "_").replace("'", "").replace("(", "").replace(")", "").replace("-", "_").replace(",", "")
    if count <= v:
        print("{\"name\": \""+ i + "\", \"index\":" + str(count) + "},")
    else:
        print("{\"name\": \""+ i + "\", \"index\":" + str(count) + ", \"default\":\"\"},")    
    # print("{\"name\": \""+ pre + i + "\", \"index\":" + str(index) + "," + "\"component_index\":" + str(count) + ", \"default\":\"\"},")
    count += 1
print()
print()

for line in f:
    i = line.lower().replace("/", "_").replace(" ", "_").replace("'", "").replace("(", "").replace(")", "").replace("-", "_")  
    print("\"" + i +"\": { \"xpath\": \"" + i +"\" },")
