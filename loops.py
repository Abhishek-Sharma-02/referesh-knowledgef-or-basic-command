
#list is a data structre which can hold multiple values of multiple type (like  string / interger / boolean / float)
#Array is a data structure which can hold multiple values of same type(like all are either string or interger or boolean or float )
list_of_cloud =["AWS", "Azure", "GCP", "Digital ocean"]

print(list_of_cloud)

#Add a new cloud in the list we can use append function, REMEBER It can only take one argument at a time and it iwll always add at the end only

list_of_cloud.append("salesforce")
list_of_cloud.append("IBM")
print("this list contain differetn cloud name: ", list_of_cloud)

# If we need to insert some item in between the list we use INSERT function and we need to provide positionn like where you want to insert

list_of_cloud.insert(3, "Heroku")  # it will insert heroku at 3 position in the list
list_of_cloud.insert(6, "Heroku")  # it will insert heroku at 6 position in the list
print("list of cloud :", list_of_cloud)

# To identify th elength of list we use len function
len(list_of_cloud)
print("the length of the list is:",len(list_of_cloud))

#Iteration of list
for cloud in list_of_cloud:
    print(cloud)


for i in range (0,8): # remember indexing start with zero so the list will  be print from 0 to 7 and not 1 to 8
    print(i)
