class MySet:


    def __init__(self, enumerable= []) -> None:
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self,value):
        #checks if the value is already included in the set and returns true or false
        #must have a run time of 0(1)
        return value in self.dictionary
        

    #print the set in a readable format using __str__
    def __str__(self) -> str:
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'
        

    def add(self,value):
        #adds value as key to collection if not present
        #run time must be 0(1)
        self.dictionary[value] = True
        return self

    def delete(self,value):
        #removes value from set and returns updated set
        #run time must be 0(1)
        self.dictionary.pop(value, None)
        return self

    def size(self):
        #returns the number of elements in the set
        return len(self.dictionary)
    

    def clear(self):
        #removes all elements from set and returns updated set
        self.dictionary.clear()

set = MySet([1,2,3])
print(set)
   
set.clear()
print(set)  