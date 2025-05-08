number_of_items = input()
products = []
pirahans_bought = 0
kapshens_bought = 0
shalvars_bought = 0
joorabs_bought = 0
for i in range(int(number_of_items)) :
    Input = input().split()
    temp_dict = {"noo" : Input[0], "rang" : Input[1], "gheymat" : int(Input[2]), "model" : Input[3]}
    products.append(temp_dict)
for j in range(len(products)) :
    if(products[j]["noo"] == "pirahan" and products[j]["gheymat"] <= 700000 and products[j]["gheymat"] >= 200000 and products[j]["model"] == "sadeh") :
        pirahans_bought += 1
    elif(products[j]["noo"] == "kapshen" and products[j]["gheymat"] <= 2000000 and products[j]["model"] == "charm" and products[j]["rang"] == "meshki") :
        kapshens_bought += 1
    elif(products[j]["noo"] == "shalvar" and products[j]["gheymat"] <= 1000000 and products[j]["gheymat"] >= 400000 and (products[j]["model"] == "jean" or products[j]["model"] == "katan") and (products[j]["rang"] == "khakestari" or products[j]["rang"] == "sabz")) :
        shalvars_bought += 1
    elif(products[j]["noo"] == "joorab" and products[j]["model"] == "nakhi" and products[j]["rang"] == "sefid") :
        joorabs_bought += 1
print(pirahans_bought)
print(kapshens_bought)
print(shalvars_bought)
print(joorabs_bought)