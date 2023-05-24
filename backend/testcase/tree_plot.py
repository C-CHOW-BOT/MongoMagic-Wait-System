
def root_plot(root, attribute, types):
    numofattribute = len(attribute)
    root_pos = numofattribute//2
    root_len = len(root)
    
    
    for i in range(len(attribute)):
        if i != root_pos:
            print(" "*(root_len+2), end = "|-")
            print(attribute[i], end = "-|-")
            print(types[i], end = "")
            print("-|-")
        else:
            print(root, end = "--|-")
            print(attribute[i], end = "-|-")
            print(types[i], end = "")
            print("-|-")
    print()



root1 = "UserSchema"
attribute1 = ["userName", "companyName", "email", "passwordEncoded", "adminPin", "profilePhoto", "siteInformation", "createdAt"]
types1 = ["String", "String", "String", "String", "String", "String", "Object", "Date"]
root_plot(root1, attribute1, types1)


root2 = "MenuSchema"
attribute2 = ["itemName", "category", "price", "description", "dietary", "thumbnail" ,"email", "translationLanguage", "options", "userId", "trsltDesp", "createdAt"]
types2 = ["String", "String", "String", "String", "Array", "String", "Object", "Object", "Object", "String", "Array", "Date"]
root_plot(root2, attribute2, types2)


root3 = "categorySchema"
attribute3 = ["userId", "email", "category"]
types3 = ["String", "String", "Object"]
root_plot(root3, attribute3, types3)


root4 = "tempOrderSchema"
attribute4 = ["siteId", "tableNumber", "order", "createdAt", "isPaid", "isCompleted", "addOn", "totalPrice", "specialRequest"]
types4 = ["String", "String", "Array", "Date", "Boolean", "Boolean", "Array", "String", "String"]
root_plot(root4, attribute4, types4)


root5 = "transactionHistorySchema"
attribute5 = ["siteId", "tableNumber", "order", "createdAt", "totalPrice"]
types5 = ["String", "String", "Array", "Date", "String"]
root_plot(root5, attribute5, types5)