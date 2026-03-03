# 1)
name=input("Enter your name: ")
print("Hello "+name)

# 2)
# Input-სა და Output-ს შორის განსხვავება ისაა რომ Input მომხმარებლისგან იღებს 
# შეყვანის მონაცემებს მაგალითად: კლავიატურას, მაუსს, კამერას, მიკროფონს და ბევრ სხვას. 
# მეორეს მხრივ Output აქვეყნებს მაგალითად პასუხს როდესაც Python-ის ტერმინალი აჩვენებს შედეგს.

# 3)
# ფუნქცია type() განსაზღვრავს რაღაცის ტიპს, მაგალითად:
test = 20
print(type(test))
# მაგალითად, ფუნქცია int() ნებისმიერ რიცხვს integer-ად გადააქცევს, 
# ფუნქცია str() ნებისმიერ ტექსტს string-ად, ფუნქცია float() ნებისმიერ რიცხვს float-ად გადააქცევს.
# მაგალითად:
test1 = 45.5 # float
test2 = 12 # integer
test3 = 200 # integer
print(int(test1)) # integer
print(float(test2)) # float
print(str(test3)) # string

# 4
abc=input("Enter your name :")
abcd=input("Enter your second name: ")
abcde=float(input("Enter your age: "))
print("Hello, your name is "+abc+" your second name is "+abcd+" and your age is",abcde,".")