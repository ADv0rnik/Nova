# import random
#
#
# def sort_items(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1):
#             if lst[i] < lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#
#
# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         q = random.choice(nums)
#         m_nums = []
#         s_nums = []
#         e_nums = []
#         for num in nums:
#             if num > q:
#                 m_nums.append(num)
#             elif num < q:
#                 s_nums.append(num)
#             else:
#                 e_nums.append(num)
#         return quick_sort(s_nums) + e_nums + quick_sort(m_nums)
#
#
# l = [1, 6, 3, 5, 2, 4, 8, 7]
#
# # sort_items(l)
# print(quick_sort(l))
# # print(l)
#
#
# def binary_search(lst: list[int], val: int):
#     first = 0
#     last = len(lst) - 1
#     index = -1
#
#     while (first <= last) and index == -1:
#         mid = (first + last) // 2
#         if lst[mid] == val:
#             index = mid
#         else:
#             if val > lst[mid]:
#                 first = mid + 1
#             elif val < lst[mid]:
#                 last = mid - 1
#     return index
#
#
# print(binary_search(l, 3))
from abc import ABC, abstractmethod


class BaseElement(ABC):

    @abstractmethod
    def get_element_name(self):
        pass


class BasePageCreator(ABC):

    def page(self):
        pass

    def element_a(self):
        pass

    def element_2(self):
        pass


class Image(BaseElement):
    def __init__(self, title):
        self._name = title
        self._size_limit = 256

    def get_element_name(self):
        return self._name

    def is_valid(self, size):
        return size <= self._size_limit


class Text(BaseElement):
    def __init__(self, name):
        self._name = name
        self._font = ""
        self._color = ""

    def get_element_name(self):
        return self._name

    def set_font(self, font):
        self._font = font


class PageCreator(BasePageCreator):
    def __init__(self):
        self._page = None
        self.reset()

    def reset(self):
        self._page = Page()

    def page(self):
        page = self._page
        self.reset()
        return page


class Page:
    def __init__(self):
        self._list_objs = []

    def add(self, element):
        self._list_objs.append(element)

    def __str__(self):
        return ', '.join(list(map(lambda a: a.get_element_name(), self._list_objs)))









