# -------------------------------------------------------------------------------
# Name:        test_vehicledriveinfodisplay.py
# Purpose:     The file is automatically generated by tools.
# Author:      CD QA Team
# Created:     2020-10-13 11:43
# -------------------------------------------------------------------------------
import allure
import pytest
from time import sleep
from src.codes.context import *


########################################################################################################################
#                                                                                                                      #
#                                                    创建Suite                                                          #
#                                                                                                                      #
########################################################################################################################
@pytest.fixture(scope="class", autouse=True)
@allure.suite("创建VehicleDriveInfodisplay测试套件")
def suite():
    with allure.step("打开CAN盒子"):
        open_device()
        sleep(10)
    yield suite
    with allure.step("关闭CAN盒子"):
        close_device()


########################################################################################################################
#                                                                                                                      #
#                                                    创建Function                                                       #
#                                                                                                                      #
########################################################################################################################
@pytest.fixture(scope="function", autouse=True)
def function():
    with allure.step("无"):
        pass
    yield
    with allure.step("无"):
        pass


########################################################################################################################
#                                                                                                                      #
#                                                    创建测试用例                                                        #
#                                                                                                                      #
########################################################################################################################
@allure.feature("module")
@pytest.mark.usefixtures("suite")
class TestVehicleDriveInfodisplay(object):

    @pytest.mark.usefixtures("function")
    @allure.title("ACC_续航里程800km")
    def test_vehicle_residual_mileage_acc_800(self):
        """
        Description:
            ACC_续航里程800km
        PreCondition:
            1.电源状态：ACC
        Steps:
            1.设置续航里程最大值：VCU_VhclResidualMile = 800
        Expect Result:
            1.仪表显示剩余续驶里程为800km
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_800()
            vehicle_residual_mileage_acc_800()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_acc_800())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC_续航里程400km")
    def test_vehicle_residual_mileage_acc_400(self):
        """
        Description:
            ACC_续航里程400km
        PreCondition:
            1.电源状态：ACC
        Steps:
            2.设置续航里程中间值：VCU_VhclResidualMile = 400
        Expect Result:
            2.仪表显示剩余续驶里程为400km
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_400()
            vehicle_residual_mileage_acc_400()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_acc_400())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC_续航里程0km")
    def test_vehicle_residual_mileage_acc_0(self):
        """
        Description:
            ACC_续航里程0km
        PreCondition:
            1.电源状态：ACC
        Steps:
            3.设置续航里程最小值：VCU_VhclResidualMile = 0
        Expect Result:
            3.仪表显示剩余续驶里程为0km
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_0()
            vehicle_residual_mileage_acc_0()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_acc_0())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC_续航里程---")
    def test_vehicle_residual_mileage_acc_850(self):
        """
        Description:
            ACC_续航里程---
        PreCondition:
            1.电源状态：ACC
        Steps:
            1.设置续航里程为无效值(0x321-0x3FF)：VCU_VhclResidualMile = 850
        Expect Result:
            1.仪表显示剩余续驶里程为---
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_850()
            vehicle_residual_mileage_acc_850()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_acc_850())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_续航里程800km")
    def test_vehicle_residual_mileage_ign_800(self):
        """
        Description:
            IGN_续航里程800km
        PreCondition:
            1.电源状态：IGN
        Steps:
            1.设置续航里程最大值：VCU_VhclResidualMile = 800
        Expect Result:
            1.仪表显示剩余续驶里程为800km
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_800()
            vehicle_residual_mileage_ign_800()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_ign_800())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_续航里程400km")
    def test_vehicle_residual_mileage_ign_400(self):
        """
        Description:
            IGN_续航里程400km
        PreCondition:
            1.电源状态：IGN
        Steps:
            2.设置续航里程中间值：VCU_VhclResidualMile = 400
        Expect Result:
            2.仪表显示剩余续驶里程为400km
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_400()
            vehicle_residual_mileage_ign_400()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_ign_400())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_续航里程0km")
    def test_vehicle_residual_mileage_ign_0(self):
        """
        Description:
            IGN_续航里程0km
        PreCondition:
            1.电源状态：IGN
        Steps:
            3.设置续航里程最小值：VCU_VhclResidualMile = 0
        Expect Result:
            3.仪表显示剩余续驶里程为0km
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_0()
            vehicle_residual_mileage_ign_0()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_ign_0())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_续航里程---")
    def test_vehicle_residual_mileage_ign_850(self):
        """
        Description:
            IGN_续航里程---
        PreCondition:
            1.电源状态：IGN
        Steps:
            1.设置续航里程为无效值(0x321-0x3FF)：VCU_VhclResidualMile = 850
        Expect Result:
            1.仪表显示剩余续驶里程为---
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_850()
            vehicle_residual_mileage_ign_850()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_ign_850())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF_续航里程800km")
    def test_vehicle_residual_mileage_off_800(self):
        """
        Description:
            OFF_续航里程800km
        PreCondition:
            1.电源状态：OFF
        Steps:
            1.设置续航里程最大值：VCU_VhclResidualMile = 800
        Expect Result:
            1.仪表显示剩余续驶里程为800km
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_800()
            vehicle_residual_mileage_off_800()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_off_800())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF_续航里程400km")
    def test_vehicle_residual_mileage_off_400(self):
        """
        Description:
            OFF_续航里程400km
        PreCondition:
            1.电源状态：OFF
        Steps:
            2.设置续航里程中间值：VCU_VhclResidualMile = 400
        Expect Result:
            2.仪表显示剩余续驶里程为400km
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_400()
            vehicle_residual_mileage_off_400()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_off_400())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF_续航里程0km")
    def test_vehicle_residual_mileage_off_0(self):
        """
        Description:
            OFF_续航里程0km
        PreCondition:
            1.电源状态：OFF
        Steps:
            3.设置续航里程最小值：VCU_VhclResidualMile = 0
        Expect Result:
            3.仪表显示剩余续驶里程为0km
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_0()
            vehicle_residual_mileage_off_0()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_off_0())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF_续航里程---")
    def test_vehicle_residual_mileage_off_850(self):
        """
        Description:
            OFF_续航里程---
        PreCondition:
            1.电源状态：OFF
        Steps:
            1.设置续航里程为无效值(0x321-0x3FF)：VCU_VhclResidualMile = 850
        Expect Result:
            1.仪表显示剩余续驶里程为---
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclresidualmile_850()
            vehicle_residual_mileage_off_850()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_residual_mileage_off_850())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC不显示P挡位")
    def test_actlgear_p_acc(self):
        """
        Description:
            ACC不显示P挡位
        PreCondition:
            1.电源状态：ACC
        Steps:
            1.设置P挡：VCU_ActlGear = 0x0
        Expect Result:
            1.仪表不显示挡位
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_p()
            actlgear_p_acc()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_p_acc())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_挡位P")
    def test_actlgear_p_ign(self):
        """
        Description:
            IGN_挡位P
        PreCondition:
            1.电源状态：IGN
        Steps:
            1.设置P挡：VCU_ActlGear = 0x0，停止5s
        Expect Result:
            1.仪表显示挡位在P挡
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_p()
            actlgear_p_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_p_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF不显示P挡位")
    def test_actlgear_p_off(self):
        """
        Description:
            OFF不显示P挡位
        PreCondition:
            1.电源状态：OFF
        Steps:
            1.设置P挡：VCU_ActlGear = 0x0
        Expect Result:
            1.仪表不显示挡位
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_p()
            actlgear_p_off()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_p_off())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_挡位R")
    def test_actlgear_r_ign(self):
        """
        Description:
            IGN_挡位R
        PreCondition:
            1.电源状态：IGN
        Steps:
            2.设置R挡：VCU_ActlGear = 0x1，停止5s
        Expect Result:
            2.仪表显示挡位在R挡
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_r()
            actlgear_r_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_r_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC不显示R挡位")
    def test_actlgear_r_acc(self):
        """
        Description:
            ACC不显示R挡位
        PreCondition:
            1.电源状态：ACC
        Steps:
            2.设置R挡：VCU_ActlGear = 0x1
        Expect Result:
            2.仪表不显示挡位
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_r()
            actlgear_r_acc()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_r_acc())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_挡位N")
    def test_actlgear_n_ign(self):
        """
        Description:
            IGN_挡位N
        PreCondition:
            1.电源状态：IGN
        Steps:
            3.设置N挡：VCU_ActlGear = 0x2，停止5s
        Expect Result:
            3.仪表显示挡位在N挡
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_n()
            actlgear_n_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_n_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC不显示N挡位")
    def test_actlgear_n_acc(self):
        """
        Description:
            ACC不显示N挡位
        PreCondition:
            1.电源状态：ACC
        Steps:
            3.设置N挡：VCU_ActlGear = 0x2
        Expect Result:
            3.仪表不显示挡位
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_n()
            actlgear_n_acc()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_n_acc())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_挡位D")
    def test_actlgear_d_ign(self):
        """
        Description:
            IGN_挡位D
        PreCondition:
            1.电源状态：IGN
        Steps:
            4.设置D挡：VCU_ActlGear = 0x3，停止5s
        Expect Result:
            4.仪表显示挡位在D挡
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_d()
            actlgear_d_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_d_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC不显示D挡位")
    def test_actlgear_d_acc(self):
        """
        Description:
            ACC不显示D挡位
        PreCondition:
            1.电源状态：ACC
        Steps:
            4.设置D挡：VCU_ActlGear = 0x3
        Expect Result:
            4.仪表不显示挡位
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_d()
            actlgear_d_acc()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_d_acc())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_挡位P&gt;D")
    def test_actlgear_d_ign1(self):
        """
        Description:
            IGN_挡位P&gt;D
        PreCondition:
            1.电源状态：IGN
            2.起始挡位在P挡
        Steps:
            1.设置D挡：VCU_ActlGear = 0x3
        Expect Result:
            1.仪表显示挡位在D挡
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            setactlgear_p()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_d()
            actlgear_d_ign1()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_d_ign1())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF不显示R挡位")
    def test_actlgear_r_off(self):
        """
        Description:
            OFF不显示R挡位
        PreCondition:
            1.电源状态：OFF
        Steps:
            2.设置R挡：VCU_ActlGear = 0x1
        Expect Result:
            2.仪表不显示挡位
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_r()
            actlgear_r_off()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_r_off())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_挡位D&gt;R")
    def test_actlgearr_r_ign1(self):
        """
        Description:
            IGN_挡位D&gt;R
        PreCondition:
            1.电源状态：IGN
            2.起始挡位在D挡
        Steps:
            1.设置D挡：VCU_ActlGear = 0x1
        Expect Result:
            1.仪表显示挡位在R挡
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            setactlgear_d()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_r()
            actlgearr_r_ign1()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgearr_r_ign1())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF不显示N挡位")
    def test_actlgear_n_off(self):
        """
        Description:
            OFF不显示N挡位
        PreCondition:
            1.电源状态：OFF
        Steps:
            3.设置N挡：VCU_ActlGear = 0x2
        Expect Result:
            3.仪表不显示挡位
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_n()
            actlgear_n_off()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_n_off())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_挡位P&gt;R")
    def test_actlgearr_r_ign2(self):
        """
        Description:
            IGN_挡位P&gt;R
        PreCondition:
            1.电源状态：IGN
            2.起始挡位在P挡
        Steps:
            1.设置D挡：VCU_ActlGear = 0x1
        Expect Result:
            1.仪表显示挡位在R挡
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            setactlgear_p()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_r()
            actlgearr_r_ign2()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgearr_r_ign2())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF不显示D挡位")
    def test_actlgear_d_off(self):
        """
        Description:
            OFF不显示D挡位
        PreCondition:
            1.电源状态：OFF
        Steps:
            4.设置D挡：VCU_ActlGear = 0x3
        Expect Result:
            4.仪表不显示挡位
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_d()
            actlgear_d_off()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_d_off())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_挡位D&gt;P")
    def test_actlgear_p_ign1(self):
        """
        Description:
            IGN_挡位D&gt;P
        PreCondition:
            1.电源状态：IGN
            2.起始挡位在D挡
        Steps:
            1.设置D挡：VCU_ActlGear = 0x0
        Expect Result:
            1.仪表显示挡位在P挡
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            setactlgear_d()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_p()
            actlgear_p_ign1()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgear_p_ign1())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_挡位D&gt;N")
    def test_actlgearr_n_ign1(self):
        """
        Description:
            IGN_挡位D&gt;N
        PreCondition:
            1.电源状态：IGN
            2.起始挡位在D挡
        Steps:
            1.设置D挡：VCU_ActlGear = 0x2
        Expect Result:
            1.仪表显示挡位在N挡
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            setactlgear_d()
        # 执行步骤
        with allure.step('操作步骤'):
            setactlgear_n()
            actlgearr_n_ign1()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_actlgearr_n_ign1())

    @pytest.mark.usefixtures("function")
    @allure.title("功率300kw")
    def test_vhclactlpwr_300kw_ign(self):
        """
        Description:
            功率300kw
        PreCondition:
            1.电源状态：IGN
            2.VCU_PtRdy=0x1
        Steps:
            1.设置功率最大值：VCU_VhclActlPwr =300
        Expect Result:
            1.仪表功率显示条值为300kw
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            ptrdy_on()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclactlpwr_300()
            vhclactlpwr_300kw_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vhclactlpwr_300kw_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("功率0kw")
    def test_vhclactlpwr_0kw_ign(self):
        """
        Description:
            功率0kw
        PreCondition:
            1.电源状态：IGN
            2.VCU_PtRdy=0x1
        Steps:
            2.设置功率中间值：VCU_VhclActlPwr =0
        Expect Result:
            2.仪表功率显示条值为0kw
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            ptrdy_on()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclactlpwr_0()
            vhclactlpwr_0kw_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vhclactlpwr_0kw_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("功率-200kw")
    def test_vhclactlpwr_200nkw_ign(self):
        """
        Description:
            功率-200kw
        PreCondition:
            1.电源状态：IGN
            2.VCU_PtRdy=0x1
        Steps:
            3.设置功率最小值：VCU_VhclActlPwr =-200
        Expect Result:
            3.仪表功率显示条值为-200kw
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            ptrdy_on()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclactlpwr_200n()
            vhclactlpwr_200nkw_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vhclactlpwr_200nkw_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("功率条不变")
    def test_vhclactlpwr_301kw_ign(self):
        """
        Description:
            功率条不变
        PreCondition:
            1.电源状态：IGN
            2.VCU_PtRdy=0x1
        Steps:
            1.设置功率无效值(0x1F5-0x1FF)：VCU_VhclActlPwr = 301
        Expect Result:
            1.仪表功率显示条不变
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            ptrdy_on()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclactlpwr_301()
            vhclactlpwr_301kw_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vhclactlpwr_301kw_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("功率条上半部分全亮")
    def test_vhclactlpwr_160kw_ign(self):
        """
        Description:
            功率条上半部分全亮
        PreCondition:
            1.电源状态：IGN
            2.VCU_PtRdy=0x1
        Steps:
            1.功率值大于150kw:VCU_VhclActlPwr = 160
        Expect Result:
            1.仪表功率显示条值为160kw，且显示条上部全亮
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            ptrdy_on()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclactlpwr_160()
            vhclactlpwr_160kw_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vhclactlpwr_160kw_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("功率条下半部分全亮")
    def test_vhclactlpwr_120nkw_ign(self):
        """
        Description:
            功率条下半部分全亮
        PreCondition:
            1.电源状态：IGN
            2.VCU_PtRdy=0x1
        Steps:
            2.功率值小于-100kw:VCU_VhclActlPwr = -120
        Expect Result:
            2.仪表功率显示条值为-120kw，且显示条下部全亮
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            ptrdy_on()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclactlpwr_120n()
            vhclactlpwr_120nkw_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vhclactlpwr_120nkw_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("功率100kw")
    def test_vhclactlpwr_100kw_ign(self):
        """
        Description:
            功率100kw
        PreCondition:
            1.电源状态：IGN
            2.VCU_PtRdy=0x1
        Steps:
            1.设置功率值为正常值:VCU_VhclActlPwr = 100
        Expect Result:
            1.仪表功率显示条值为100kw
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            ptrdy_on()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclactlpwr_100()
            vhclactlpwr_100kw_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vhclactlpwr_100kw_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("功率120kw")
    def test_vhclactlpwr_120kw_ign(self):
        """
        Description:
            功率120kw
        PreCondition:
            1.电源状态：IGN
            2.VCU_PtRdy=0x1
        Steps:
            1.设置功率值：VCU_VhclActlPwr = 120
            2.等待5s
            3.设置车速：ESP_VhclSpd=11
        Expect Result:
            1.仪表显示功率为120kw
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            ptrdy_on()
        # 执行步骤
        with allure.step('操作步骤'):
            vhclactlpwr_120()
            sleep(5)
            vehiclespeed_10()
            vhclactlpwr_120kw_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vhclactlpwr_120kw_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("车速0km/h")
    def test_vehicle_speed_0_ign(self):
        """
        Description:
            车速0km/h
        PreCondition:
            1.电源状态：IGN
            2.ESP_VhclSpd_Vld =0x1
        Steps:
            1.设置最小车速：ESP_VhclSpd = 0 
        Expect Result:
            1.仪表显示车速为0km/h
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            vehiclespeed_0()
            vehicle_speed_0_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_speed_0_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("车速1km/h")
    def test_vehicle_speed_1_ign(self):
        """
        Description:
            车速1km/h
        PreCondition:
            1.电源状态：IGN
            2.ESP_VhclSpd_Vld =0x1
        Steps:
            2.设置车速在(0,1)：ESP_VhclSpd = 0.5
        Expect Result:
            2.仪表显示车速为1km/h
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            vehiclespeed_0_5()
            vehicle_speed_1_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_speed_1_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("车速2km/h")
    def test_vehicle_speed_2_ign(self):
        """
        Description:
            车速2km/h
        PreCondition:
            1.电源状态：IGN
            2.ESP_VhclSpd_Vld =0x1
        Steps:
            3.设置车速在[1,2):   ESP_VhclSpd = 1.5
        Expect Result:
            3.仪表显示车速为2km/h
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            vehiclespeed_1_5()
            vehicle_speed_2_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_speed_2_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("车速72km/h")
    def test_vehicle_speed_72_ign(self):
        """
        Description:
            车速72km/h
        PreCondition:
            1.电源状态：IGN
            2.ESP_VhclSpd_Vld =0x1
        Steps:
            4.设置车速在[2,+):  ESP_VhclSpd =  70
        Expect Result:
            4.仪表显示车速为72km/h
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            vehiclespeed_70()
            vehicle_speed_72_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_speed_72_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("无效车速")
    def test_vehicle_speed_100_inv_ign(self):
        """
        Description:
            无效车速
        PreCondition:
            1.电源状态：IGN
            2.设置车速为0
        Steps:
            1.设置车速任意值：ESP_VhclSpd = 100
        Expect Result:
            1.仪表显示车速为0km/h
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            vehiclespeed_0()
        # 执行步骤
        with allure.step('操作步骤'):
            vehiclespeed_100_invalid()
            sleep(1)
            vehicle_speed_100_inv_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_speed_100_inv_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("车速超过最大值，无效车速")
    def test_vehicle_speed_301_ign(self):
        """
        Description:
            车速超过最大值，无效车速
        PreCondition:
            1.电源状态：IGN
            2.ESP_VhclSpd_Vld =0x1
        Steps:
            1.设置车速为无效值(0x14D7-0x1FFF）)：ESP_VhclSpd = 301
        Expect Result:
            1.仪表显示车速为0km/h
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            vehiclespeed_301()
            vehicle_speed_301_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_vehicle_speed_301_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC_SOC进度条绿色")
    def test_disp_soc_100_acc(self):
        """
        Description:
            ACC_SOC进度条绿色
        PreCondition:
            1.电源状态：ACC
        Steps:
            1.设置电量最大值：VCU_DispSoc = 100
        Expect Result:
            1.仪表电量进度条显示为满格，颜色为绿色
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_100()
            disp_soc_100_acc()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_100_acc())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC_SOC进度条红色")
    def test_disp_soc_4_acc(self):
        """
        Description:
            ACC_SOC进度条红色
        PreCondition:
            1.电源状态：ACC
        Steps:
            2.设置电量低于5%：VCU_DispSoc = 4
        Expect Result:
            2.仪表电量进度条显示为4，颜色为红色
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_4()
            disp_soc_4_acc()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_4_acc())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC_SOC为0")
    def test_disp_soc_0_acc(self):
        """
        Description:
            ACC_SOC为0
        PreCondition:
            1.电源状态：ACC
        Steps:
            3.设置电量最小值：VCU_DispSoc = 0
        Expect Result:
            3.仪表电量进度条显示为0
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_0()
            disp_soc_0_acc()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_0_acc())

    @pytest.mark.usefixtures("function")
    @allure.title("ACC_SOC值超过最大值，显示0")
    def test_disp_soc_101_acc(self):
        """
        Description:
            ACC_SOC值超过最大值，显示0
        PreCondition:
            1.电源状态：ACC
        Steps:
            1.设置电量无效值0x65~0x7F：VCU_DispSoc = 101
        Expect Result:
            1.仪表电量进度条显示为0
        """
        # 前置条件
        with allure.step("前置条件"):
            power_acc()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_101()
            disp_soc_101_acc()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_101_acc())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF_SOC进度条绿色")
    def test_disp_soc_100_off(self):
        """
        Description:
            OFF_SOC进度条绿色
        PreCondition:
            1.电源状态：OFF
        Steps:
            1.设置电量最大值：VCU_DispSoc = 100
        Expect Result:
            1.仪表电量进度条显示为满格，颜色为绿色
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_100()
            disp_soc_100_off()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_100_off())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF_SOC进度条红色")
    def test_disp_soc_4_off(self):
        """
        Description:
            OFF_SOC进度条红色
        PreCondition:
            1.电源状态：OFF
        Steps:
            2.设置电量低于5%：VCU_DispSoc = 4
        Expect Result:
            2.仪表电量进度条显示为4，颜色为红色
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_4()
            disp_soc_4_off()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_4_off())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF_SOC为0")
    def test_disp_soc_0_off(self):
        """
        Description:
            OFF_SOC为0
        PreCondition:
            1.电源状态：OFF
        Steps:
            3.设置电量最小值：VCU_DispSoc = 0
        Expect Result:
            3.仪表电量进度条显示为0
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_0()
            disp_soc_0_off()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_0_off())

    @pytest.mark.usefixtures("function")
    @allure.title("OFF_SOC值超过最大值，显示0")
    def test_disp_soc_101_off(self):
        """
        Description:
            OFF_SOC值超过最大值，显示0
        PreCondition:
            1.电源状态：OFF
        Steps:
            4.设置电量无效值0x65~0x7F：VCU_DispSoc = 101
        Expect Result:
            1.仪表电量进度条显示为0
        """
        # 前置条件
        with allure.step("前置条件"):
            power_off()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_101()
            disp_soc_101_off()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_101_off())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_SOC进度条绿色")
    def test_disp_soc_100_ign(self):
        """
        Description:
            IGN_SOC进度条绿色
        PreCondition:
            1.电源状态：IGN
        Steps:
            1.设置电量最大值：VCU_DispSoc = 100
        Expect Result:
            1.仪表电量进度条显示为满格，颜色为绿色
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_100()
            disp_soc_100_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_100_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_SOC进度条红色")
    def test_disp_soc_4_ign(self):
        """
        Description:
            IGN_SOC进度条红色
        PreCondition:
            1.电源状态：IGN
        Steps:
            2.设置电量低于5%：VCU_DispSoc = 4
        Expect Result:
            2.仪表电量进度条显示为4，颜色为红色
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_4()
            disp_soc_4_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_4_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_SOC为0")
    def test_disp_soc_0_ign(self):
        """
        Description:
            IGN_SOC为0
        PreCondition:
            1.电源状态：IGN
        Steps:
            3.设置电量最小值：VCU_DispSoc = 0
        Expect Result:
            3.仪表电量进度条显示为0
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_0()
            disp_soc_0_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_0_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("IGN_SOC值超过最大值，显示0")
    def test_disp_soc_101_ign(self):
        """
        Description:
            IGN_SOC值超过最大值，显示0
        PreCondition:
            1.电源状态：IGN
        Steps:
            1.设置电量无效值0x65~0x7F：VCU_DispSoc = 101
        Expect Result:
            1.仪表电量进度条显示为0
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_101()
            disp_soc_101_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_101_ign())

    @pytest.mark.usefixtures("function")
    @allure.title("SOC进度条黄色")
    def test_disp_soc_50_ign(self):
        """
        Description:
            SOC进度条黄色
        PreCondition:
            1.电源状态：OFF
            2.BCU_BattCpLowWarn = 0x1 
        Steps:
            1.设置电量：VCU_DispSoc = 50
        Expect Result:
            1.仪表电量进度条显示为50，颜色为黄色
        """
        # 前置条件
        with allure.step("前置条件"):
            power_ign()
            bcu_battcplowwarn_lists_open()
        # 执行步骤
        with allure.step('操作步骤'):
            battery_surplus_display_50()
            disp_soc_50_ign()
        # 期望结果
        with allure.step('期望结果'):
            compare(compare_disp_soc_50_ign())
