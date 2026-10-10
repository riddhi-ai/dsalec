#Accept two values S and N . Print square of first N numbers starting from S like if S is 11 and N is 5 then print square from 11 till 15

S=int(input("Enter the value of S : "))
N=int(input("Enter the value of N :"))

for i in range(S, S + N):   
    print(f"Square of {i} is {i*i}")  #using fstring

