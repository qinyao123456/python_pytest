import pytest
'''
 pytest 默认寻找当前路径下所有的文件与子文件夹中以test开头的文件夹、文件、函数作为识别对象
 pytest 默认不输出任何打印信息，如果要看打印信息，需要在运行时添加-s的指令
 多指令一同运行时，需要通过空格进行区分，在main函数中，是通过,进行分割
 -v  用于详细显示日志信息
 -rA  测试结果的简单统计
'''
# def setup_function():
#     print('开始了')
# def teardown_function():
#     print('结束了')
def setup_module():
    print('module')
def teardown_module():
    print('module')
def test_01(xuzhu):
    print('test01')

def test_02(xuzhu):
    print('test02')
def test_03(xuzhu):
    print('test_03')
def test_04(xuzhu01):
    assert xuzhu01 ==1,'断言失败'

#pytest 中class对象的定义：建议以test开头
class TestDemo:
    def setup(self):
        print('我们是祖国的花朵')
    def teardown(self):
        print('我们是祖国的花朵')
    def test_d1(self):
        print('你好')
    def test_d2(self):
        print('您好')
if __name__ == '__main__':
    #-v  类似输出日志
    # pytest.main(['-s','test_case.py::test_02','-v'])
    pytest.main(['-s','-v','-rA'])