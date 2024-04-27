x={"name":"John","age":30}
y=x.copy()
x["name"]="Jane"
print(y["name"])


#Name won't change when copy is taken before
#It will change when copy is taken after that