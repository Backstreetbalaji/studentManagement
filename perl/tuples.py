Tuple = tuple((1, 3, 3, 2, 4, 6, 7, 8, 9))
print("Original list ", Tuple)


class Tuple_class:
    def __int__(self):
        pass

    # Reverse the Tuple list1
    def reverse(self):
        tuple_list1 = list(Tuple)
        tuple_list1.reverse()
        reversed_tuple = tuple(tuple_list1)
        print("Reverse for Tuple ", reversed_tuple)
        tuple_list1.reverse()
        Ori_tuple = tuple(tuple_list1)
        print("Original for Tuple ", Ori_tuple)

    # Copy the one Tuple list to another Tuple list
    def copy(self):
        tuple_list = list(Tuple)
        tuple_list2 = tuple_list.copy()
        Ori_tuple = tuple(tuple_list2)
        print("Copy of Tuple_list1 in Tuple_list2 ", tuple_list2)

    # Multiply by 10 in tuple list element
    def mulbyten(self):
        list1 = list(Tuple)
        a = 10
        list2 = []
        for x in list1:
            list2.append(x * a)
            tuple_list2 = tuple(list2)
            print("Multiply by 10 for Tuple ", tuple_list2)

    # divided by 10 in tuple list element
    def divbyten(self):
        list1 = list(Tuple)
        a = 10
        list1[:] = [x / a for x in list1]
        tuple_list2 = tuple(list1)
        print("divide by 10 for Tuple ", tuple_list2)

    # Add element in tuple both sides
    def add(self):
        list1 = list(Tuple)
        list1.insert(0, 100)
        print("add value first element in Tuple ", list1)

        list1.append(100)
        tuple_list2 = tuple(list1)
        print("add value in last element Tuple ", tuple_list2)

    # Remove element in tuple both sides
    def remove(self):
        list1 = list(Tuple)
        del list1[0]
        print("remove value first element in Tuple ", list1)

        list1.pop(-1)
        tuple_list2 = tuple(list1)
        print("remove value in last element Tuple ", tuple_list2)

    # check the average tuple
    def average(self):
        list1 = list(Tuple)
        Average = sum(list1) / len(list1)
        print("Average value of Tuple ", Average)

    # Find the odd element in tuple
    def odd(self):
        list1 = list(Tuple)
        for x in list1:
            if x % 2 != 0:
                odd_list = [x]
                tuple_list2 = tuple(odd_list)
                print("Odd value of Tuple ", tuple_list2)

    # Find the even element in tuple
    def even(self):
        list1 = list(Tuple)
        list1 = [x for x in list1 if x % 2 == 0]
        tuple_list2 = tuple(list1)
        print("Even value of Tuple ", tuple_list2)


obj = Tuple_class()
obj.reverse()
obj.copy()
obj.mulbyten()
obj.divbyten()
obj.add()
obj.remove()
obj.average()
obj.odd()
obj.even()