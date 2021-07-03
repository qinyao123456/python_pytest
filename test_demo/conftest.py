'''
这是pytest中的预置函数定义的配置文件,注意：文件名称一定是conftest,不能是其他的
scope参数定义的4种等级(默认等级是function)
  session:在本次session级别中只执行一次
  module:在模块级别中只执行一次
  class:在类级别中只执行一次
  function:在函数级别中国执行，每有一个函数就执行一次
pytest中的setup和teardown：一般可以通过一个配置文件直接进行管理：配置文件命名一定要是conftest.py
'''
import pytest

#预置函数 用于前期的数据准备
@pytest.fixture(scope='function')
def xuzhu():
    print('虚竹很强')
def xuzhu01():
    return 1
