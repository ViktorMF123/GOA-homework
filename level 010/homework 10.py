# 1)
# boolean არის მდგომარეობა როდესაც რაღაც ან მართალია ან მცდარია 1 ან 0.

# 2) 3)
# ლოგიკური ოპერატორებია არიან or and და not, მაგალითად:
nub1=20
nub2=3
print(nub1>nub2 or nub2>nub1) # True
print(nub1>nub2 or nub2<nub1) # True
print(nub1>nub2 and nub2>nub1) # False
print(nub1>nub2 and nub2<nub1) # True
print(True and True) # True
print(True or True) # True
print(True or False) # True
print(False or False) # False
print(False and True) # False
print(False and False) # False
if not nub1<nub2: # True
    print("test")

# 4)
# ლოგიკური ოპერატორები რეალურ ცხოვრებასთან
# მსგავსია რადგან იგივე სიტუაციების ხელახლა შექმნა შესაძლებელია.