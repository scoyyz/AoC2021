#Part 1
# depths = []

# with open("Day1.txt") as file:
  # depths = file.readlines()
  # file.close()
  
# i = 0
# increases = 0
# print(len(depths))

# while i < len(depths):
  # if i > 0:
    # if int(depths[i].strip()) > int(depths[i-1].strip()):
      # increases += 1
    # else:
      # print(depths[i-1].strip()+"-->"+depths[i].strip())
  # i+=1

# print(increases)  

#Part 2
depths = []

with open("Day1.txt") as file:
    depths = file.readlines()
    file.close()

i = 0
while i < len(depths):
    temp = depths[i].strip()
    depths[i]=int(temp)
    i+=1
    
i = 3
increases = 0

while i < len(depths):
  window1 = depths[i-3]+depths[i-2]+depths[i-1]
  window2 = depths[i-2]+depths[i-1]+depths[i]
  if window2 > window1:
    increases+=1
  i+=1

print(increases)