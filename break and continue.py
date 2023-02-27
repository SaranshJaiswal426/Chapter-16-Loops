i = 0
while i < 7:
 print(i)
 if i == 4:
   print("Breaking from loop")
 break
 i += 1
 break

for i in (0, 1, 2, 3, 4, 5):
 if i == 2 or i == 4:
  continue
 print(i) 