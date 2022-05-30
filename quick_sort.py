from characteristics import *
import functools
from enum import Enum,auto
import random

tshirt_list=[]
colors = ["red","orange","yellow","green","indigo","violet"] 
#sizes=["s","m","l","xl","xxl","xxxl"]
fabrics=['wool','cotton','polyester','rayon','linen','cashmere','silk']

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

def quick_sort(t_shirt_list):
    def partition(t_shirt_list, start, finish):
         pivot = t_shirt_list[start]
         less = [elem for elem in t_shirt_list[start+1:finish+1] if elem < pivot]
         greaterequal = [elem for elem in t_shirt_list[start+1:finish + 1] if elem >= pivot]
         new_array = less + [pivot] + greaterequal
         for i in range(start, finish+1):
             t_shirt_list[i]=new_array.pop(0)
         return start + len(less)
    def quick_sort_rec(t_shirt_list, start, finish):
         if start < finish:
             pos = partition(t_shirt_list,start,finish)
             quick_sort_rec(t_shirt_list,start,pos-1)
             quick_sort_rec(t_shirt_list,pos+1,finish)
    quick_sort_rec(t_shirt_list,0,len(t_shirt_list)-1)

def random_color(x):
    for i in range(x): 
        random_color = random.choice(colors)
        random_size = random.choice(sizes)
        random_fabric = random.choice(fabrics)
        not_so_random_price = FabricPrice(random_fabric).calc()
        tshirt = [random_color,random_size,random_fabric,not_so_random_price]
        i+=1
        tshirt_list.append(tshirt)

    return tshirt_list

def random_size(x):
    for i in range(x): 
        random_color = random.choice(colors)
        random_value = random.randrange(1,6)
        #random_size = Sizes(random_value).name
        random_fabric = random.choice(fabrics)
        not_so_random_price = FabricPrice(random_fabric).calc()
        tshirt = [random_value,random_color,random_fabric,not_so_random_price]
        i+=1
        tshirt_list.append(tshirt)

    return tshirt_list

def random_fabric(x):
    for i in range(x): 
        random_color = random.choice(colors)
        random_size = random.choice(sizes)
        random_fabric = random.choice(fabrics)
        not_so_random_price = FabricPrice(random_fabric).calc()
        tshirt = [random_fabric,random_color,random_size,not_so_random_price]
        i+=1
        tshirt_list.append(tshirt)

    return tshirt_list
    
# sort by color asc
def sorting_color_asc(x):
    t_list = random_color(x)
    quick_sort(t_list)
    for t in range(len(t_list)):
        print(t_list[t])

# sorting_color(10)

# sort by color desc
def sorting_color_desc(x):
    t_list = random_color(x)
    quick_sort(t_list)
    for t in range(len(t_list)-1,-1,-1):
        print(t_list[t])

# sort by size asc
def sorting_size_asc(x):
    t_list = random_size(x)
    quick_sort(t_list)
    for t in t_list:
        t[0] = Sizes(t[0]).name
        print(t,sep=',')

# sorting_size(10)

# sort by size desc
def sorting_size_desc(x):
    t_list = random_size(x)
    quick_sort(t_list)
    for t in sorted(t_list, key=lambda x:x[0], reverse=True):
        t[0] = Sizes(t[0]).name
        print(t,sep=',')

# sort by fabric asc
def sorting_fabric_asc(x):
    t_list = random_fabric(x)
    quick_sort(t_list)
    for t in t_list:
        print(t)

# sorting_fabric(10)

# sort by fabric desc
def sorting_fabric_desc(x):
    t_list = random_fabric(x)
    quick_sort(t_list)
    for t in sorted(t_list, key=lambda x:x[0], reverse=True):
        print(t)