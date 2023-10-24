#########################################################################
# 作者:李宁（蒙娜丽宁），UnityMarvel创始人
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################

import asyncio
import time

async def greet(delay, msg):
    await asyncio.sleep(delay)
    print('hello',msg)

async def main():
    print("开始执行")
    startTime = time.time()
    await greet(1, 'Bill')
    await greet(2, 'Mike')
    print("运行时间:",time.time()-startTime)
    print("运行结束")

asyncio.run(main())
# 判断函数是否为协程函数
print(asyncio.iscoroutinefunction(greet))
print(asyncio.iscoroutinefunction(main))


