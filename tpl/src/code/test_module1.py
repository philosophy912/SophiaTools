# -------------------------------------------------------------------------------
# Name:        test_module1.py
# Purpose:     The file is automatically generated by tools.
# Author:      CD QA Team
# Created:     2020-10-07 09:29
# -------------------------------------------------------------------------------
import allure
import pytest
from time import sleep
from automotive import *
from src.code.context import Tester

tester = Tester()


########################################################################################################################
#                                                                                                                      #
#                                                    创建Suite                                                          #
#                                                                                                                      #
########################################################################################################################
@pytest.fixture(scope="class", autouse=True)
@allure.suite("创建module1测试套件")
def suite():
    with allure.step("打开设备"):
        tester.battery_test1()
    yield suite
    with allure.step("关闭设备"):
        sleep(3)


########################################################################################################################
#                                                                                                                      #
#                                                    创建Function                                                       #
#                                                                                                                      #
########################################################################################################################
@pytest.fixture(scope="function", autouse=True)
def function():
    with allure.step("发送CAN信号"):
        tester.battery_test1()
    yield
    with allure.step("恢复CAN信号"):
        pass


########################################################################################################################
#                                                                                                                      #
#                                                    创建测试用例                                                        #
#                                                                                                                      #
########################################################################################################################
@allure.feature("module")
@pytest.mark.usefixtures("suite")
class TestModule1(object):

    @pytest.mark.usefixtures("function")
    @allure.title("测试用例1")
    def test_testcase1(self):
        """
        Description:
            testcase1
        PreCondition:
            condition1
        Steps:
            steps1
        Expect Result:
            expect1
        """
        # 前置条件
        with allure.step("前置条件"):
            tester.battery_test1()
        # 执行步骤
        with allure.step('操作步骤'):
            tester.can_test1()
        # 期望结果
        with allure.step('期望结果'):
            result = tester.info1()
            if len(result) > 1:
                result, images, compare_type, dark, light = result
                if compare_type == CompareTypeEnum.LIGHT:
                    allure.attach.file(light, '原图(亮图)', allure.attachment_type.BMP)
                elif compare_type == CompareTypeEnum.DARK:
                    allure.attach.file(dark, '原图(暗图)', allure.attachment_type.BMP)
                elif compare_type == CompareTypeEnum.BLINK:
                    allure.attach.file(light, '原图(亮图)', allure.attachment_type.BMP)
                    allure.attach.file(dark, '原图(暗图)', allure.attachment_type.BMP)
                result_str = "成功" if result else "失败"
                for image in images:
                    image_name = image.split("\\")[-1]
                    allure.attach.file(image, f"{result_str}截图[{image_name}]", allure.attachment_type.BMP)
                assert result
            else:
                assert result
