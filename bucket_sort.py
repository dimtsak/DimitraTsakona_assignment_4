from characteristics import *
import functools
from enum import Enum,auto
import random


#colors = ["red","orange","yellow","green","indigo","violet"] 
#sizes=["s","m","l","xl","xxl","xxxl"]
#fabrics=['wool','cotton','polyester','rayon','linen','cashmere','silk']

@functools.total_ordering
class Sizes(Enum):
    S = auto()
    M = auto()
    L = auto()
    XL = auto()
    XXL = auto()
    def __gt__(self,other):
        return self.value > other.value
    
sizes = []
sizes_values = []
for size in Sizes:
    sizes.append(size.name)
    sizes_values.append(size.value)
# print(sizes)
# print(sizes_values)

@functools.total_ordering
class Fabrics(Enum):
    
    silk = auto()
    cashmere = auto()
    linen = auto()
    cotton = auto()
    wool = auto()
    polyester = auto()
    rayon = auto()
    
    def __gt__(self,other):
        return self.value > other.value

fabrics = []
fabrics_values = []
for fabric in Fabrics:
    fabrics.append(fabric.name)
#     fabrics_values.append(fabric.value)
# print(fabrics)
# print(fabrics_values)
    
class Colors(Enum):
    green = auto()
    indigo = auto()
    orange = auto()
    red = auto()
    violet = auto()
    yellow = auto()
    
    def __gt__(self,other):
        return self.value > other.value

colors = []
colors_values = []
for color in Colors:
    colors.append(color.name)
    colors_values.append(color.value)
# print(colors)
# print(colors_values)

def bucketSort(a,maxVal):
    bucket= [None]*(maxVal+1)   # create a number of buckets
    for i in range(len(bucket)):
        bucket[i]=0             # initialize buckets with 0
    for i in range(len(a)):
        bucket[a[i]]+=1         # insert all a elements to buckets
    outPos=0
    for i in range(len(bucket)):
        for j in range(bucket[i]):
            a[outPos]=i
            outPos+=1


def random_tshirts(x):
    tshirt_list=[]
    for i in range(x): 
        # random_color = random.choice(colors)
        # random_size = random.choice(sizes)
        # random_fabric = random.choice(fabrics)
        random_color = random.randrange(1,7)
        random_size = random.randrange(1,6)
        random_fabric = random.randrange(1,8)
        fabric_price = FabricPrice(Fabrics(random_fabric).name).calc()
        tshirt = [random_size,random_color,random_fabric,fabric_price]
        i+=1
        tshirt_list.append(tshirt)

    return tshirt_list
   
# sort by color asc
def sorting_color_asc(x, maxVal):
    t_list = random_tshirts(x)
    # print(t_list)
    color_sort_list = []
    size_rand_list = []
    fabric_rand_list = []
    price_rand_list = []
    for element in t_list:
        color_sort_list.append(element[0])
        size_rand_list.append(element[1])
        fabric_rand_list.append(element[2])
        price_rand_list.append(element[3])
    bucketSort(color_sort_list, maxVal)
    new_list = [None]*x
    for item in range(len(color_sort_list)):
        random_size = random.randrange(1,6)
        random_fabric = random.randrange(1,8)
        fabric_price = FabricPrice(Fabrics(random_fabric).name).calc()
        new_list[item]=[color_sort_list[item],random_size,random_fabric,fabric_price]
    # print(new_list)
    # print("-"*20)
    
    for j in new_list:
        j[0]=Colors(j[0]).name
        j[1]=Sizes(j[1]).name
        j[2]=Fabrics(j[2]).name
        print(j,sep=',')

# sort by color desc
def sorting_color_desc(x,maxVal):
    t_list = random_tshirts(x)
    color_sort_list = []
    size_rand_list = []
    fabric_rand_list = []
    price_rand_list = []
    for element in t_list:
        color_sort_list.append(element[0])
        size_rand_list.append(element[1])
        fabric_rand_list.append(element[2])
        price_rand_list.append(element[3])
    bucketSort(color_sort_list, maxVal)
    new_list = [None]*x
    for item in range(len(color_sort_list)):
        random_size = random.randrange(1,6)
        random_fabric = random.randrange(1,8)
        fabric_price = FabricPrice(Fabrics(random_fabric).name).calc()
        new_list[item]=[color_sort_list[item],random_size,random_fabric,fabric_price]
    
    for j in sorted(new_list, key=lambda x:x[0], reverse=True):
        j[0]=Colors(j[0]).name
        j[1]=Sizes(j[1]).name
        j[2]=Fabrics(j[2]).name
        print(j,sep=',')

# sort by size asc
def sorting_size_asc(x, maxVal):
    t_list = random_tshirts(x)
    size_sort_list = []
    color_rand_list = []
    fabric_rand_list = []
    price_rand_list = []
    for element in t_list:
        size_sort_list.append(element[0])
        color_rand_list.append(element[1])
        fabric_rand_list.append(element[2])
        price_rand_list.append(element[3])
    bucketSort(size_sort_list, maxVal)
    new_list = [None]*x
    for item in range(len(size_sort_list)):
        random_color = random.randrange(1,7)
        random_fabric = random.randrange(1,8)
        fabric_price = FabricPrice(Fabrics(random_fabric).name).calc()
        new_list[item]=[size_sort_list[item],random_color,random_fabric,fabric_price]
    
    for j in sorted(new_list, key=lambda x:x[0], reverse=False):
        j[0]=Sizes(j[0]).name
        j[1]=Colors(j[1]).name
        j[2]=Fabrics(j[2]).name
        print(j,sep=',')

# sort by size desc
def sorting_size_desc(x, maxVal):
    t_list = random_tshirts(x)
    size_sort_list = []
    color_rand_list = []
    fabric_rand_list = []
    price_rand_list = []
    for element in t_list:
        size_sort_list.append(element[0])
        color_rand_list.append(element[1])
        fabric_rand_list.append(element[2])
        price_rand_list.append(element[3])
    bucketSort(size_sort_list, maxVal)
    new_list = [None]*x
    for item in range(len(size_sort_list)):
        random_color = random.randrange(1,7)
        random_fabric = random.randrange(1,8)
        fabric_price = FabricPrice(Fabrics(random_fabric).name).calc()
        new_list[item]=[size_sort_list[item],random_color,random_fabric,fabric_price]
    
    for j in sorted(new_list, key=lambda x:x[0], reverse=True):
        j[0]=Sizes(j[0]).name
        j[1]=Colors(j[1]).name
        j[2]=Fabrics(j[2]).name
        print(j,sep=',')

# sort by fabric asc
def sorting_fabric_asc(x, maxVal):
    t_list = random_tshirts(x)
    # print(t_list)
    color_rand_list = []
    size_rand_list = []
    fabric_sort_list = []
    price_rand_list = []
    for element in t_list:
        fabric_sort_list.append(element[0])
        color_rand_list.append(element[1])
        size_rand_list.append(element[2])
        price_rand_list.append(element[3])
    bucketSort(fabric_sort_list, maxVal)
    new_list = [None]*x
    for item in range(len(fabric_sort_list)):
        random_color = random.randrange(1,7)
        random_size = random.randrange(1,6)
        fabric_price = FabricPrice(Fabrics(fabric_sort_list[item]).name).calc()
        new_list[item]=[fabric_sort_list[item],random_color,random_size,fabric_price]
    
    for j in sorted(new_list, key=lambda x:x[0], reverse=False):
        j[0]=Fabrics(j[0]).name
        j[1]=Colors(j[1]).name
        j[2]=Sizes(j[2]).name
        print(j,sep=',')

# sort by fabric desc
def sorting_fabric_desc(x, maxVal):
    t_list = random_tshirts(x)
    # print(t_list)
    color_rand_list = []
    size_rand_list = []
    fabric_sort_list = []
    price_rand_list = []
    for element in t_list:
        fabric_sort_list.append(element[0])
        color_rand_list.append(element[1])
        size_rand_list.append(element[2])
        price_rand_list.append(element[3])
    bucketSort(fabric_sort_list, maxVal)
    new_list = [None]*x
    for item in range(len(fabric_sort_list)):
        random_color = random.randrange(1,7)
        random_size = random.randrange(1,6)
        fabric_price = FabricPrice(Fabrics(fabric_sort_list[item]).name).calc()
        new_list[item]=[fabric_sort_list[item],random_color,random_size,fabric_price]
    
    for j in sorted(new_list, key=lambda x:x[0], reverse=True):
        j[0]=Fabrics(j[0]).name
        j[1]=Colors(j[1]).name
        j[2]=Sizes(j[2]).name
        print(j,sep=',')

