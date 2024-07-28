#File-handling is a way to store the data in a file and read/write the data from the file.
#There are 4 modes to open a file:
#1. r-read mode- This mode is used to read the data from the file
#2. w-write mode- This mode is used to write the data in the file
#3. a-append mode - This mode is used to append the data in the file
#4. r+-read and write mode - This mode is used to read and write the data in the file
#5. w+-write and read mode - This mode is used to write and read the data in the file
#6. a+-append and read mode - This mode is used to append and read the data in the file
#7. x-create mode - This mode is used to create the file
#8. t-text mode - This mode is used to open the file in text mode
#9. b-binary mode - This mode is used to open the file in binary mode
#10. + - This mode is used to open the file in read and write mode

#Opening a file
# file=open("MyFile","w") #opening a file in write mode
# file.write("Hello, This is Adarsh") #writing the data in the file
# file.write("\nName: Adarsh\nAge: X\nAddress: XYZ", ) 
# file.close()
# print("File created successfully.")

#Reading the data from the file
file1=open("MyFile","r") #opening a file in read mode
# print("Data in the file is:",file1.read()) #reading the data from the file
print("First line- ",file1.readline(),end='') #reading the first line from the file
print("Second line- ",file1.readline(), end='') #reading the second line from the file
print("first 12 character- ",file1.read(12)) #reading the first character from the file
# print("First 10 characters=",file1.readline(10),end='')


#Appending the data in the file
file2=open("MyFile","a") #opening a file in append mode
file2.write("\nThis is the appended data.") #appending the data in the file
print(file1.read())

file1.close()
file2.close()   