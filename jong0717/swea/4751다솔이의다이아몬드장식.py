T = int(input())
for t in range(T):
    my_str = input()
    line1 = '..'+'...'.join('#'*len(my_str))+'..'
    line2 = '.#'*(len(my_str)*2)+'.'
    line3 = '#.'+'.#.'.join(my_str)+'.#'
    # print(line1)
    # print(line2)
    # print(line3)
    print('{0}\n{1}\n{2}\n{1}\n{0}'.format(line1,line2,line3))