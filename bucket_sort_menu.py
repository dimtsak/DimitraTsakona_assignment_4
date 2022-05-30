from bucket_sort import *

def main():
    while True:
        # num = int(input("\nPlease input the number of random T-shirts you want: \t"))
        # maxVal = int(input("\nEnter the number of buckets: \t"))
        num = 40
        maxVal = 20
        print("\nYour cart contains ", num," t-shirts:")
        menu = input('''\n\t\tChoose a sorting option:
                        1 --> By Color
                        2 --> By Size
                        3 --> By Fabric: \t''')
        while menu not in ['1', '2', '3']:
            print("\nPlease enter a valid option for menu:\n")
            menu = input('''\n\t\tChoose a sorting option:
                        1 --> By Color
                        2 --> By Size
                        3 --> By Fabric: \t''')
        if menu == '1':           
            order = (input('''Choose sorting order:\n
                                1 --> Ascending
                                2 --> Descending
                                3 --> back: \t'''))
            while order not in ['1','2','3']:
                print("\nNot a valid sorting order")
                order = (input('''Choose sorting order:\n
                                1 --> Ascending
                                2 --> Descending
                                3 --> back: \t'''))
            if order == '1':  
                print("T-shirts sorted by color in ascending order: ")
                print("(color, size, fabric, price in euros)")
                sorting_color_asc(num, maxVal)
            elif order == '2':
                print("T-shirts sorted by color in descending order: ")
                print("(color, size, fabric, price in euros)")
                sorting_color_desc(num, maxVal)
            elif order == '3':
                main()
        elif menu == '2':           
            order = (input('''Choose sorting order:\n
                                1 --> Ascending
                                2 --> Descending
                                3 --> back: \t'''))
            while order not in ['1','2','3']:
                print("\nNot a valid sorting order")
                order = (input('''Choose sorting order:\n
                                1 --> Ascending
                                2 --> Descending
                                3 --> back: \t'''))
            if order == '1':  
                print("T-shirts sorted by size in ascending order: ")
                print("(size, color, fabric, price in euros)")
                sorting_size_asc(num, maxVal)
            elif order == '2':
                print("T-shirts sorted by size in descending order: ")
                print("(size, color, fabric, price in euros)")
                sorting_size_desc(num, maxVal)
            elif order == '3':
                main()
        elif menu == '3':           
            order = (input('''Choose sorting order:\n
                                1 --> Ascending
                                2 --> Descending
                                3 --> back: \t'''))
            while order not in ['1','2','3']:
                print("\nNot a valid sorting order")
                order = (input('''Choose sorting order:\n
                                1 --> Ascending
                                2 --> Descending
                                3 --> back: \t'''))
            if order == '1':  
                print("T-shirts sorted by fabric in ascending order: ")
                print("(fabric, color, size, price in euros)")
                sorting_fabric_asc(num, maxVal)
            elif order == '2':
                print("T-shirts sorted by fabric in descending order: ")
                print("(fabric, color, size, price in euros)")
                sorting_fabric_desc(num, maxVal)
            elif order == '3':
                main()
            

if __name__ == "__main__":
    main()
