# python文件用来统一执行所有的测试用例
import unittest


#如果这个文件不是最初的启动文件.那么main函数代码快中的语句将不能执行
if __name__ == '__main__':
    #1.找到所有的测试用例
    #discover发现所有的测试用例.这句话的意思
    test_cases=unittest.defaultTestLoader.discover(".", pattern='*Test.py', top_level_dir=None)
    #2.执行这些测试用例
    #TextTestRunner文本 的测试用例运行器
    #run 执行.;/这句话的意思是执行测试用例,并且生成文本的结果.并且在控制台中显示文本的结果
    unittest.TextTestRunner().run(test_cases)











