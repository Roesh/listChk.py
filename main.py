print("I'm assuming your lists contain unique values ([1,2,3]), haven't tested this on lists with duplicates ([1,2,2])")

list1 = [1,2,3,4]
list2 = [5,6,7,8]

list1n2 = [] #Items in list 1, but not 2
list2n1 = [] #Items in list 2, but not 1
list1u2 = [] #Items in both list 1 and 2

def inputList(listName):
  tmp = input("Input " + listName + " . <Enter> to use internal list: ")
  tmp = tmp.strip()
  if len(tmp) is 0:
    return None
  tmplist = []
  while len(tmp) is not 0:
    tmplist.append(tmp)
    tmp = input("Next value? ")
    tmp = tmp.strip()
  return tmplist

tmplist = inputList("list 1")
if tmplist is not None:
  list1 = tmplist
print(list1)

tmplist = inputList("list 2")
if tmplist is not None:
  list2 = tmplist
print(list2)

if len(list1) is not len(list2):
  print("FYI, list lengths don't match.")

list2n1 = list(list2)
for x in list1:
  list1n2.append(x)
  for y in list2:    
    if str(x) == str(y):
      list1u2.append(x)
      try:
        list1n2.remove(x)
      except:
        pass
      try:
        list2n1.remove(x)
      except:
        pass
print(len(list1u2), "values match between lists")
print(len(list1n2), "values in list 1 but not 2")
print(len(list2n1), "values in list 2 but not 1")

def menu():
  tmp = input("""
    1) Union list
    2) Values in 1 not 2
    3) Values in 2 not 1
    4) Write to files
    5) Quit
    Print what? """)
  tmp = tmp.strip()
  if len(tmp) is 0:
    return tmp
  try: 
    tmp = int(tmp)
  except:
    tmp = "0" #Return 0
  return str(tmp)

def printVals(l,of=None):
  if of is not None:
    stro = ''
    for x in l:
      stro = stro+str(x)+'\n'
    of.write(stro)
    return
  for x in l:
    print(str(x))

tmp = menu()
while(len(tmp) is not 0):
  if int(tmp) is 1:
    printVals(list1u2)
  if int(tmp) is 2:
    printVals(list1n2)
  if int(tmp) is 3:
    printVals(list2n1)   
  if int(tmp) is 4:
    fname = input("base filename?")
    try:      
        of = open(fname+'_union.txt','w')
        printVals(list1u2,of)
        of.close()
        of = open(fname+'_1n2.txt','w')
        printVals(list1n2,of)
        of.close()
        of = open(fname+'_2n1.txt','w')
        printVals(list2n1,of)
        of.close()
    except:
      print("Could not write to files")    
  if int(tmp) is 5:  
    quit()
  tmp = menu()