# 二分查找, 快速乘

# 快速幂
# 举个例子：3**42 
#1. 将42二进制拆分
# 42 = （101010）2 = 1 * 2**5 + 0  * 2 ** 4 + ... + 0 * 2**0
# 再代入到3的幂中
# 得出： 求解a**b的时候，如果b是奇数，那么原式就是: a * a ** b-1
# 如果b是偶数， 原式变成： a**b/2 * a**b/2 
# 这样我们就把原来的 
# 算法就被优化成了，的算法， 这就是快速幂的实现原理
# 算法可以用递归来实现
# int qpow(int a,int b)
# {
#     if(!b)
#         return 1;
#     else if(b&1)
#         return a*qpow(a,b-1);
#     else
#     {
#         int t=qpow(a,b>>1); # b >> 1 也代表除以2（因为题目不允许用除法）
#         return t*t;
#     }
# }

# 但递归常熟较大， 所以采用迭代的写法
# 我们会发现，无论b为何值，它在快速幂迭代的过程中要么-1，要么除以2
# 但无论它采用了以上的哪一种操作，都必会有一个时刻，b = 1
# 也就是说，b在迭代的过程中，至少会有一个时刻b为奇数
# 那么我们考虑，我们完全可以在 b / 2 的迭代中，先不使迭代的结果影响到答案，而是先把迭代的结果储存下来，
# 然后等到 b 为奇数的时候统一加到答案里去。这样就省去了繁琐的递归和记录答案的过程，保证了常数小，而且维护了答案的正确性。
# int qpow(int a,int b)
# {
#     int ret=1;
#     while(b>0)
#     {
#         if(b&1) # 当b是奇数时
#             ret*=a; # 直接加到答案里
            # 这样就省去了繁琐的递归和记录答案的过程，保证了常数小，而且维护了答案的正确性。
#         a*=a;
#         b>>=1;
#         }
#     }
#     return ret;
# }


# 快速乘
# def qmult(a, b, mod):
#     ret = 0
#     while b > 0:
#         if b & 1:
#             ret = (ret + a) % mod
#         a = (a + a) % mod
#         b >>= 1
#     return ret

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN: # 被除数 = -2**31
            if divisor == 1: # 除数
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        
        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0
        
        # 一般情况，使用二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        # 也就是说答案一定会是从1~2**31 之间
        # 如果binary search 无效，则答案归 0
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        # 快速乘
        def quickAdd(y: int, z: int, x: int) -> bool:
            # x 和 y 是负数，z 是正数
            # 需要判断 z * y >= x 是否成立
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1: # check if z is odd number or not
                    # 需要保证 result + add >= x
                    if result < x - add: # 检查是否小于， 否则会溢出
                        return False
                    result += add
                if z != 1: # 不是奇数，则进行快速乘相加
                    # 需要保证 add + add >= x
                    if add < x - add: # 一样如果溢出，直接返回False
                        return False
                    add += add
                # 不能使用除法
                z >>= 1 # 除以2
            return True
        
        left, right, ans = 1, INT_MAX, 0 # 由于我们先前处理，把所有除数和被除数都弄成负数，所以答案一定是正数，即范围介于1~2**31-1
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1) # 找midpoint，二分查找常规步骤
            check = quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                # 注意溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return -ans if rev else ans 
    
sol = Solution()
print(sol.divide(32, 16))