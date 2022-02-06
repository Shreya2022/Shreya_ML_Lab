# Find-S Algorithm:
import csv
a = []
with open('finds.csv') as csfile:
    reader = csv.reader(csfile)
    for row in reader:
        a.append(row)
        print(row)
num_attributes=len(a[0])-1 #num_attributes = 6

print("The most general hypothesis:",["?"]*num_attributes)
print("The most specific hypothesis:",["0"]*num_attributes)

hypothesis=a[0][:-1]
print(hypothesis)
print("\n Find S: Finding a maximally specific hypothesis")
for i in range (len(a)):
    print(i)
    print(num_attributes)
    if a[i][num_attributes] == "Yes":
        for j in range(num_attributes):
            # print(j)
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
    print("The taining example no:",i+1," the hyposthesis is:",hypothesis)
print("\n The maximally specific hypohthesis for training set is")
print(hypothesis)