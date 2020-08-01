'''
计算数字三角形从上到下和最大的路径
比如：[[1],[2,4],[4,5,6]]，最大路径是1-4-6，输出值是11
'''

#方法1：递归计算
#i,j为起点，若是找全局的，就是（0,0）
#递归计算的调用次数很多，存在重复调用，效率很低。2^n次
def Recursion(i,j,a):
    n = len(a)-1
    if i==n:
        return a[i][j]
    s = Recursion(i+1,j,a)
    t = Recursion(i+1,j+1,a)
    return a[i][j]+ max(s,t)

#方法2：记忆化搜索
#原理，计算过的值把他保存下来，避免反复计算
def RememberRecur(i,j,a):


def NumTriangle(Matrix):
    print(Recursion(0,0,Matrix))


if __name__ == "__main__":
    Matrix =[[1],[2,4],[4,5,6]]
    NumTriangle(Matrix)