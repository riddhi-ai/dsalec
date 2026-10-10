n = 5  # number of rows

for i in range(1, n + 1):  #outer loop
   
    print(" " * (n - i) + "* " * i)  # print spaces first then stars 
    # print(" " * (n - i) + "*" * i) this creates the pyramid left aligned if not given sppaces in star
