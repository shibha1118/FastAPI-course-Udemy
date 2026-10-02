my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

count = 0
while count<3:
    count+=1
    for x in my_list:
        if x == "Monday":
            continue 
        print(x)
        