class list1:

    def reverse(self):
        # Reverse a list in Python
        list_1 = [10, 20, 30, 40, 50]
        # list_1.reverse()
        # print(list_1)

        # type 2
        list_1 = list_1[::-1]
        print(list_1)

    def concatenate_Index(self):
        list_1 = ["m", "na", "i", "Ha"]
        list_2 = ["y", "me", "s", "ri"]
        list_3 = [i + j for i, j in zip(list_1, list_2)]
        print(list_3)

    def item_Square(self):
        list_1 = [1, 2, 3, 4, 5, 6, 7]
        list_1 = [i * i for i in list_1]
        print(list_1)

        # type 2
        list_2 = [1, 2, 3, 4, 5, 6, 7]
        list_3 = []
        for i in list_2:
            list_3.append(i * i)
        print(list_3)

    def concatenate_two_lists(self):
        list_1 = ["Hello ", "take "]
        list_2 = ["Dear", "Sir"]
        list_3 = [i + j for i in list_1 for j in list_2]
        print(list_3)

    def lists_simultaneously(self):
        list_1 = [10, 20, 30, 40]
        list_2 = [100, 200, 300, 400]
        for i, j in zip(list_1, list_2[::-1]):
            print(i, j)

    def remove_sting(self):
        list_1 = ["My", "Name", "", "is", "Hari"]
        list_2 = list(filter(None, list_1))
        print(list_2)

    def add_new_elem(self):
        list_1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
        list_1[2][2].append(7000)
        print(list_1)

    def adding_sublist(self):
        list_1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
        list_2 = ["h", "i", "j"]
        list_1[2][1][2].extend(list_2)
        print(list_1)

    def replaceandpastevaluefound(self):
        list1 = [5, 10, 15, 20, 25, 50, 20]
        # get the first occurrence index
        index = list1.index(20)

        # update item present at location
        list1[index] = 200
        print(list1)

    def deleteaccerence(self):
        list1 = [5, 20, 15, 20, 25, 50, 20]

        # remove specific items and return a new list
        def remove_value(list2, val):
            return [x for x in list2 if x != val]

        res = remove_value(list1, 20)
        print(res)


list1 = list1()
list1.reverse()
list1.concatenate_Index()
list1.item_Square()
list1.concatenate_two_lists()
list1.lists_simultaneously()
list1.remove_sting()
list1.add_new_elem()
list1.adding_sublist()
list1.replaceandpastevaluefound()
list1.deleteaccerence()