def atlagos_elegedettseg():

    nums = ()
    iter = list(nums)  
    iter.append(int(input()))  

    nums = tuple(iter)
    for iter in range(3):
            iter = list(nums)  
            iter.append(int(input()))  

            nums = tuple(iter)
    
    print(sum(nums)/len(nums))
if __name__ == "__main__":
    atlagos_elegedettseg()