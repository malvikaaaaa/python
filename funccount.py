def count_string(strg):
    count=0
    for item in strg.split():
        if len(item)>1 and item[0]==item[-1]:
            count=count+1
    return count

strg=input("Enter a collection of strings:")
print("count of string:",count_string(strg))
