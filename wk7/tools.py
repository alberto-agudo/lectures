# Example taken from Gries et al. 2013. Practical Programming: An Introduction
# to Computer Science Using Python 3

def main():
    ls = [1, 2, 3]
    running_sum(ls)
    print('Running sum of [1, 2, 3] is:', ls)

def running_sum(ls):
    '''Modify ls so that it contains the running sums of its original items.
    E.g., running_sum([1, 2, 3]) becomes [1, 3, 6].'''
    for i in range(len(ls)):
        ls[i] = ls[i - 1] + ls[i]
        
    # The way to solve this issue is by using range(1, len(ls)), since the i-1 was generating the problems 
    #(if i == 0 then we would be selecting the last element of the list instead of the first one).

if __name__ == '__main__':
    main()
