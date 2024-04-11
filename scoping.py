max_a = [1]
diameter_a = 1
def just_a_function():
    # nonlocal max_a # will not work, same scope
    # nonlocal diameter_a # will not work, same scope
    print(max_a)
    print(diameter_a)
    return
just_a_function()
class Solution:
    cache = []
    def fn(self):
        max_b = [3]
        def inner_scope():
            nonlocal max_b
            max_b += [43]
            print(max_b)
        inner_scope()
sol = Solution()
x = sol.fn()
print(x)