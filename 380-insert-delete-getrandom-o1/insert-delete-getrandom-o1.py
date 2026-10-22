import random
class RandomizedSet:

    def __init__(self):
        self.val_to_index={}
        self.list=[]

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val]=len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        last_element=self.list[-1]
        idx_to_remove=self.val_to_index[val]

        self.list[idx_to_remove]=last_element
        self.val_to_index[last_element]=idx_to_remove

        self.list.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()