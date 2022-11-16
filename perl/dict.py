class dictionary:

    def zipfun(self):
        # Convert two lists into a dictionary
        keys = ['Hari', 'Naveen', 'balaji']
        values = [100, 200, 300]
        res_dict = dict(zip(keys, values))
        print(res_dict)

    def updatefun(self):
        # Convert two lists into a dictionary
        keys = ['Hari', 'Naveen', 'balaji']
        values = [100, 200, 300]
        # empty dictionary
        New_dict = dict()

        for i in range(len(keys)):
            New_dict.update({keys[i]: values[i]})
            print(New_dict)

    def twoinone(self):
        # Merge two Python dictionaries into one
        dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
        dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

        dict3 = {**dict1, **dict2}
        print(dict3)


    def nestedkey(self):
        # Print the value of key ‘history’ from the below dict
        pathDict = {
            "class": {
                "student": {
                    "name": "Rio",
                    "marks": {
                        "salary": 10000,
                        "marks": 90
                    }
                }
            }
        }

        # solution of select a key in nested value of Dict
        print(pathDict['class']['student']['marks']['salary'])

    def fromkey(self):
        # Initialize dictionary with default values
        employees = ['Hari', 'Naveen']
        position = {"designation": 'XPP Developer', "salary": 50000}

        dict4 = dict.fromkeys(employees, position)
        print(dict4)

        # Individual data selection
        print(dict4["Hari"])

    def extractkey(self):
        # Create a dictionary by extracting the keys from a given dictionary
        exDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
        keys = ["name", "salary"]

        NewDict = {k: exDict[k] for k in keys}
        print(NewDict)

    def deletekey(self):
        exDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
        # Keys to remove
        keys = ["name", "salary"]
        # Using the pop() method and loop
        for k in keys:
            exDict.pop(k)
        print(exDict)

        # Dictionary Comprehension
        exDict1 = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
        exDict1 = {k: exDict1[k] for k in exDict1.keys() - keys}
        print(exDict1)

    def checkvalue(self):
        # Check if a value exists in a dictionary
        dict6 = {'a': 100, 'b': 200, 'c': 300}

        if 200 in dict6.values():
            print('200 present in a dict')

    def renamekey(self):
        # Rename key of a dictionary
        exDict1 = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
        exDict1['location'] = exDict1.pop('city')
        print(exDict1)

    def minimumvalue(self):
        # Get the key of a minimum value from the following dictionary
        exDict2 = {'Physics': 82, 'Math': 65, 'history': 75}
        print(min(exDict2, key=exDict2.get))

    def changevaluekey(self):
        # Change value of a key in a nested dictionary
        sample_dict = {
            'emp1': {'name': 'hari', 'salary': 7500},
            'emp2': {'name': 'Naveen', 'salary': 8000},
            'emp3': {'name': 'Balaji', 'salary': 50000}
        }
        sample_dict['emp3']['salary'] = 8500
        print(sample_dict)


obj = dictionary()
obj.zipfun()
obj.updatefun()
obj.twoinone()
obj.nestedkey()
obj.fromkey()
obj.extractkey()
obj.deletekey()
obj.checkvalue()
obj.renamekey()
obj.minimumvalue()
obj.changevaluekey()