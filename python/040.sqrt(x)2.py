# 牛顿迭代
# 牛顿迭代法是一种可以用来快速求解函数零点的方法
# 我们用 C 表示待求出平方根的那个整数。显然，C 的平方根就是函数
# y = f(x) = x^2 − C 的零点
# 牛顿迭代法的本质是借助泰勒级数，从初始值开始快速向零点逼近
# 我们任取一个 x0  作为初始值，在每一步的迭代中，我们找到函数图像上的点 (xi,f(xi))
# 过该点作一条斜率为该点导数 f′(xi) 的直线,与横轴的交点记为 xi+1
# x i+1 相较于 xi 而言距离零点更近。在经过多次迭代后，我们就可以得到一个距离零点非常接近的交点

# 算法
# 我们选择 x0=C 作为初始值
# 在每一步迭代中，我们通过当前的交点 xi，找到函数图像上的点 (xi,xi2−C)
# 作一条斜率为 f′(xi)=2xi 的直线，直线的方程为:
# yl =2xi(x−xi)+x^2−C (quadratic equation: y = mx + c, m = f'(xi) = 2xi, x = (x-xi), C = x^2 - C)
# 与横轴的交点为方程 2xix−(xi^2+C)=0 的解，即为新的迭代结果 xi+1：
# xi+1 = 1/2 * (xi + (C/xi))
# 在进行 k 次迭代后，xk 的值与真实的零点 sqrt. C 足够接近，即可作为答案

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        C, x0 = float(x), float(x)
        while True:
            xi = (x0 + C / x0) / 2
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        
        return int(x0)


sol = Solution()
print(sol.mySqrt(25))