#count the vowels from the accepted sentence

sentence = input("Enter the sentence: ")
vowels = "aeiouAEIOU"
count = 0
for characters in sentence:
    if characters in vowels:
        count += 1 #adds the number of vowels in sentence

print("Number of vowels:", count)
