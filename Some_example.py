def swap_case(a):
    return a.swapcase()


# Here we can define the next lines of the code as we can see
# This is the line that we can use in the next lines of the code|
def some_func(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


###### This is the simple manner to call inside the functions #####
if __name__ == '__main__':
    s = input()
    the_res = swap_case(s)
    print(the_res)
