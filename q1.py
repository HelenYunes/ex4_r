
class bounded_subsets:
    
    
    def __init__(self, src, sum):
        self.sum,sum_0 = sum,0
        self.list = sorted(src)
        self.curr_list, self.members = 0,0
        for num in self.list:
            if num > sum:
                self.list.remove(num)
            if sum_0 > self.sum:
                break
            sum_0 = sum_0 + num
            self.members += 1
            
    def __iter__(self):
        return self

    def __next__(self):
        next,list_0 = True, []
        while next:
            next = False
            if self.curr_list >= pow(2, len(self.list)):  #all combinations (of inner numbers)
                raise StopIteration
            curr_sub = "{0:b}".format(self.curr_list).zfill(len(self.list))  # create the current sub ( binary format)
            self.curr_list = self.curr_list + 1
            if sum(map(lambda s, l: int(s) * l, curr_sub, self.list)) <= self.sum:
                for e in range(0, len(self.list)):
                    if curr_sub[e] != "0":
                        list_0.append(self.list[e])
                return list_0
            next = True
 
if __name__ == '__main__':
        print("Example number 1:")
        for s in bounded_subsets([1, 2, 3], 4):
            print(s)
        print("Example number 2")
      
        for s in bounded_subsets([1, 2, 3], 6):
            print(s)
        print("Example number 3")

        for s in bounded_subsets([1, 2, 3,4], 12):
            print(s)
    