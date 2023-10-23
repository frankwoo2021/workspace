#########################################################################
# 作者:李宁（蒙娜丽宁）
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################

from cffi import FFI

ffi = FFI()

so = ffi.dlopen("./libadd.so")
ffi.cdef("int add(int a, int b);")
print(so.add(10, 20))