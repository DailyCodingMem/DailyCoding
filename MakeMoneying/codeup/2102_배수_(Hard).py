N = int(input())

String = 1
List = [String] # ['1']

if int(String)%N:

    flag = 1
    while flag:
        Result = []
        for i in range(len(List)):
            A = int(str(List[i])+'1')
            if A > 18446744073709551615:
                print(0)
                flag = 0
                break
            Result.append(A)
            if not int(A)%N:
                print(int(A))
                flag = 0
                break

            A = int(str(List[i])+'0')
            if A > 18446744073709551615:
                print(0)
                flag = 0
                break
            Result.append(A)
            if not int(A)%N:
                print(int(A))
                flag = 0
                break


        Result.sort()
        List = Result
else:
    print(int(String))