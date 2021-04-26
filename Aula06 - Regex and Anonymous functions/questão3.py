"""
3. Aplique a função math.fmod a todos os elementos da lista nums, de forma que os ítens
sejam copiados para uma nova lista, porém só com as 3 casas decimais. nums = [1.1765,
1.98387, 5.9364976, 7.845289, 3.9998871]
"""

import math
nums = [1.1765, 1.98387, 5.9364976, 7.845289, 3.9998871]
nums2= list(map(lambda x: math.fmod(int(x*1000), 1000)/1000, nums))
print(nums2, "\n", nums)
