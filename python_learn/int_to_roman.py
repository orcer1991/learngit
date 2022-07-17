import os

class solution:
    def int_to_roman(self, num:int)->str:
        a , b , c , d = num//1000, num%1000//100,num%100//10,num%10
        ge =  ['', 'I' , 'II' , 'III' ,'IV' , 'V' ,'VI', 'VII' , 'VIII' , 'IX']
        
        shi = ['', 'X' , 'XX' , 'XXX' ,'XL' , 'L' ,'LX' , 'LXX', 'LXXX', 'XC']
        
        bai = ['', 'C' , 'CC' , 'CCC' ,'CD' , 'D' ,'DC' , 'DCC', 'DCCC', 'CM']

        qian = ['' , 'M' , 'MM' , 'MMM']

        str1 = ''

        str1 = qian[a] + bai[b] + shi[c] + ge[d]
        return str1


if "__main__" == __name__:
    t = solution()
    x = int(input())
    ret = t.int_to_roman(x)
    print(ret)
