beatles = [] # step 1
print("Step 1:", beatles)

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Herrison')
# step 2
print("Step 2:", beatles)

for i in range(2):
    new_member = input('Please add latercomer members one-by-one (Stu Sutcliffe, Pete Best): ')# step 3
    beatles.append(new_member)
print("Step 3:", beatles)
    

for i in range(2):
    del beatles[len(beatles)-1]# step 4
print("Step 4:", beatles)

beatles.insert(0,'Ringo Starr')# step 5
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
