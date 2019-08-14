# -*- coding:utf-8 -*-


class Common(object):
    @staticmethod
    def similar(a, b, similar_range):
        return a - similar_range <= b <= a + similar_range

    @staticmethod
    def remove_similar(l, similar_range):
        list_len = len(l) - 1
        i = 0
        while i < list_len:
            if Common.similar(l[i], l[i + 1], similar_range):
                list_len -= 1
                del (l[i + 1])
            else:
                i += 1
