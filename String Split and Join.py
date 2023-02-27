

def split_and_join(line):
    arr=line.split()
    ans="-".join(arr)
    return ans

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
