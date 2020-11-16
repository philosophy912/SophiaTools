package com.chinatsp.automotive.utils;

import com.chinatsp.automotive.entity.BaseEntity;
import com.chinatsp.automotive.entity.actions.ElementAction;
import com.chinatsp.automotive.entity.actions.RelayAction;
import com.chinatsp.automotive.entity.actions.ScreenOpsAction;
import com.chinatsp.automotive.entity.actions.ScreenShotAction;
import com.chinatsp.automotive.entity.collection.Element;
import com.chinatsp.automotive.entity.compare.ImageCompare;
import com.chinatsp.automotive.entity.compare.InformationCompare;
import com.chinatsp.automotive.entity.storage.Information;
import com.chinatsp.automotive.entity.testcase.TestCase;
import com.chinatsp.automotive.enumeration.DeviceTpeEnum;
import com.chinatsp.automotive.enumeration.ElementOperationTypeEnum;
import com.chinatsp.automotive.enumeration.RelayOperationTypeEnum;
import com.chinatsp.automotive.enumeration.ScreenOperationTypeEnum;
import com.chinatsp.automotive.enumeration.ScreenShotTypeEnum;
import com.chinatsp.automotive.enumeration.TestCaseFunctionTypeEnum;
import com.chinatsp.dbc.entity.Message;
import com.chinatsp.dbc.entity.Signal;
import com.philosophy.base.common.Pair;
import com.philosophy.base.util.StringsUtils;
import com.philosophy.character.util.CharUtils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static com.chinatsp.automotive.utils.Constant.EQUAL;

/**
 * @author lizhe
 * @date 2020/9/7 13:22
 **/
@Component
@Slf4j
public class CheckUtils {


    /**
     * 函数名检查是否正确（python）
     *
     * @param name 函数名
     * @return true：正确 false：不正确
     */
    private boolean isFunctionCorrect(String name) {
        int max = 255;
        String regex = "[a-zA-Z]+[a-zA-Z0-9_]*";
        boolean isMatch = name.matches(regex);
        if (name.length() > max) {
            return false;
        } else {
            return isMatch;
        }
    }

    /**
     * 函数名是否正确
     * 仅支持长度小于100的英文字符数字和下划线组成的图片名且后缀不能带_
     *
     * @param name 函数名
     * @return true：正确 false：不正确
     */
    private boolean isImageNameCorrect(String name) {
        if (name.contains("__")) {
            return false;
        }
        int max = 100;
        String regex = "^[a-zA-Z0-9]+[a-zA-Z_0-9]*[^_]$";
        boolean isMatch = name.matches(regex);
        if (name.length() > max) {
            return false;
        } else {
            return isMatch;
        }
    }

    /**
     * 图片全名是否正确
     * 仅支持长度小于100的英文字符数字和下划线组成的JPG、PNG、BMP图片
     *
     * @param name 图片名
     * @return true：正确 false：不正确
     */
    private boolean isFullImageNameCorrect(String name) {
        int max = 100;
        String regex = "^[a-zA-Z0-9]+[a-zA-Z_0-9]*[^_](.)((bmp)|(jpg)|(png))$";
        boolean isMatch = name.matches(regex);
        if (name.length() > max) {
            return false;
        } else {
            return isMatch;
        }
    }

    /**
     * 根据名字获取signal
     *
     * @param message    can消息列表
     * @param signalName 信号名
     * @return 信号对象
     */
    private Signal getSignal(Message message, String signalName) {
        for (Signal signal : message.getSignals()) {
            if (signal.getName().equals(signalName)) {
                return signal;
            }
        }
        return null;
    }

    /**
     * 根据ID获取message
     *
     * @param messages  can消息列表
     * @param messageId 消息ID
     * @return 消息对象
     */
    private Message getMessage(List<Message> messages, Long messageId) {
        for (Message message : messages) {
            if (message.getId() == messageId) {
                return message;
            }
        }
        return null;
    }

    /**
     * 根据Signal的名字查找Message
     *
     * @param messages   can消息列表
     * @param signalName 信号名字
     * @return 消息对象
     */
    public Message getMessage(List<Message> messages, String signalName) {
        for (Message message : messages) {
            for (Signal signal : message.getSignals()) {
                if (signal.getName().equals(signalName)) {
                    return message;
                }
            }
        }
        return null;
    }

    /**
     * 检查CAN的value是否符合要求
     * todo 需要计算因子，这个地方都传入的是物理值，非总线值
     *
     * @param i           第几行
     * @param className   表sheet的名字
     * @param signalName  信号名称
     * @param signalSize  信号长度
     * @param signalValue 信号值
     */
    private void checkCanValue(int i, String className, String signalName, Integer signalSize, Long signalValue) {
        Double max = Math.pow(2, signalSize);
        if (signalValue > max) {
            String error = "Sheet[" + className + "]的第" + i + "行数据填写错误，CAN信号" + signalName + "设置的值超过了最大范围";
            throw new RuntimeException(error);
        }
    }


    /**
     * 检查实体类中的某个属性的值是否符合python对于函数的命名规范
     *
     * @param name      要校验的内容
     * @param index     行号
     * @param className 类名
     */
    public void checkPythonFunction(String name, int index, String className) {
        if (!isFunctionCorrect(name)) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "必须符合python命名规则， 当前名字是" + name;
            throw new RuntimeException(error);
        }
    }

    /**
     * 检查截图名称，仅支持英文+下划线方式，不支持数字已经.jpg类似的格式
     */
    public void checkScreenshotName(String name, int index, String className) {
        if (!isImageNameCorrect(name)) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "图片名只能是小于100个字符的英文字符或者下划线且不能以下划线结尾且不能有连续__的下划线存在, 当前图片名为" + name;
            throw new RuntimeException(error);
        }
    }

    /**
     * 检查截图名称，图片名必须是完整的图片名，且图片仅支持英文字符和下划线方式命名的JPG、BMG、PNG图片
     */
    public void checkTemplateImage(String name, int index, String className) {
        if (!isFullImageNameCorrect(name)) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "图片名必须是完整的图片名，且图片仅支持英文字符和数字和下划线组合方式命名的JPG、BMG、PNG图片, 当前图片名为[" + name + "]";
            throw new RuntimeException(error);
        }
    }


    /**
     * 检查点击的点是否在屏幕范围内
     *
     * @param screenOpsAction 截屏对象
     * @param index           行号
     * @param className       类名
     * @param qnxWidth        qnx的宽
     * @param qnxHeight       qnx的高
     * @param androidWidth    android的宽
     * @param androidHeight   android的高
     */
    public void checkClickPoints(ScreenOpsAction screenOpsAction, int index, String className,
                                 int qnxWidth, int qnxHeight, int androidWidth, int androidHeight) {
        List<Pair<Integer, Integer>> points = screenOpsAction.getPoints();
        for (Pair<Integer, Integer> pair : points) {
            int x = pair.getFirst();
            int y = pair.getSecond();
            int maxWidth;
            int maxHeight;
            if (screenOpsAction.getDeviceType() == DeviceTpeEnum.QNX) {
                maxWidth = qnxWidth;
                maxHeight = qnxHeight;
            } else {
                maxWidth = androidWidth;
                maxHeight = androidHeight;
            }
            if (x <= 0 || x >= maxWidth) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                        x + "必须在小于等于" + maxWidth;
                throw new RuntimeException(error);
            }
            if (y <= 0 || y >= maxHeight) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                        y + "必须在小于等于" + maxHeight;
                throw new RuntimeException(error);
            }
        }
    }

    /**
     * 检查点击的点是否在屏幕范围内
     *
     * @param imageCompare  图片对比
     * @param index         行号
     * @param className     类名
     * @param qnxWidth      qnx的宽
     * @param qnxHeight     qnx的高
     * @param androidWidth  android的宽
     * @param androidHeight android的高
     */
    public void checkClickPositions(ImageCompare imageCompare, int index, String className,
                                    int qnxWidth, int qnxHeight, int androidWidth, int androidHeight) {
        List<Integer[]> positions = imageCompare.getPositions();
        DeviceTpeEnum type = imageCompare.getDeviceType();
        int maxWidth;
        int maxHeight;
        if (type == DeviceTpeEnum.QNX) {
            if (qnxWidth == -1 || qnxHeight == -1) {
                String error = "请检查Sheet[配置(Configure)]中的[QNX屏幕宽高]填写是否正确";
                throw new RuntimeException(error);
            }
            maxWidth = qnxWidth;
            maxHeight = qnxHeight;
        } else {
            if (androidWidth == -1 || androidHeight == -1) {
                String error = "请检查Sheet[配置(Configure)]中的[Android屏幕宽高]填写是否正确";
                throw new RuntimeException(error);
            }
            maxWidth = androidWidth;
            maxHeight = androidHeight;
        }
        for (Integer[] position : positions) {
            int x = position[0];
            int y = position[1];
            int width = position[2];
            int height = position[3];

            if (x <= 0 || x >= maxWidth || y <= 0 || y >= maxHeight || x + width > maxWidth || y + height >= maxHeight) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，请检查坐标点以及高宽填写是否符合要求";
                throw new RuntimeException(error);
            }
        }
    }

    /**
     * 检查屏幕数量是否符合要求
     *
     * @param screenShotAction  ScreenShotAction表格
     * @param index             行号
     * @param className         类名
     * @param maxAndroidDisplay 最多的安卓屏幕数量
     * @param maxQnxDisplay     最多的QNX屏幕数量
     */
    public void checkDisplay(ScreenShotAction screenShotAction, int index, String className, int maxAndroidDisplay, int maxQnxDisplay) {
        ScreenShotTypeEnum type = screenShotAction.getScreenShotType();
        int displayId = screenShotAction.getDisplayId();
        if (type == ScreenShotTypeEnum.ANDROID_DISPLAY) {
            if (displayId <= 0 || displayId > maxAndroidDisplay) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                        "屏幕数量必须小于" + maxAndroidDisplay + "个";
                throw new RuntimeException(error);
            }
        } else if (type == ScreenShotTypeEnum.QNX_DISPLAY) {
            if (displayId <= 0 || displayId > maxQnxDisplay) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                        "屏幕数量必须小于" + maxQnxDisplay + "个";
                throw new RuntimeException(error);
            }
        }

    }

    /**
     * 检查继电器通道数量是否符合要求
     *
     * @param relayAction 继电器操作
     * @param index       行号
     * @param className   类名
     * @param maxChannel  最多的通道
     */
    public void checkRelayChannel(RelayAction relayAction, int index, String className, int maxChannel) {
        RelayOperationTypeEnum type = relayAction.getRelayOperationType();
        if (type == RelayOperationTypeEnum.OFF || type == RelayOperationTypeEnum.ON) {
            int channel = relayAction.getChannelIndex();
            if (channel == 0) {
                String error = "Sheet[" + className + "]的第" + index + "行的操作为[" + type.getValue() + "]，该操作必须填写继电器通道号";
                throw new RuntimeException(error);
            }
            if (channel <= 0 || channel > maxChannel) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，继电器通道数必须小于等于" + maxChannel + "个";
                throw new RuntimeException(error);
            }
        }
    }

    /**
     * 检查电源操作的电流电压值是否符合要求
     *
     * @param voltages  电流电压值
     * @param index     行号
     * @param className 类名
     * @param maxValue  最大值
     * @param minValue  最小值
     */
    public void checkBatteryValue(Double[] voltages, int index, String className, double minValue, double maxValue) {
        log.debug("minValue = {}, maxValue = {}", minValue, maxValue);
        if (voltages.length != 1) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，电流或电压只能设置一个值";
            throw new RuntimeException(error);
        }
        Double startVoltage = voltages[0];
        if (startVoltage < minValue || startVoltage > maxValue) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，设置电压" + startVoltage + "超过了[" + minValue + ", " + maxValue + "]";
            throw new RuntimeException(error);
        }
    }

    /**
     * 检查电源操作的调节值是否符合要求
     *
     * @param voltages  电源集合
     * @param index     行号
     * @param className 类名
     * @param maxValue  最大值
     * @param minValue  最小值
     */
    public void checkBatteryAdjust(Double[] voltages, int index, String className, double minValue, double maxValue) {
        if (voltages.length != 4) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "电压调节设置模式为其实起始电压-终止电压-步进值-间隔时间, 当前值为" + Arrays.toString(voltages);
            throw new RuntimeException(error);
        }
        Double startVoltage = voltages[0];
        Double endVoltage = voltages[1];
        Double step = voltages[2];
        Double maxStep = maxValue - minValue;
        if (startVoltage < minValue || startVoltage > maxValue) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "设置电压" + startVoltage + "超过了[" + minValue + "," + maxValue + "]";
            throw new RuntimeException(error);
        }
        if (endVoltage < minValue || endVoltage > maxValue) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "设置电压" + startVoltage + "超过了[" + minValue + "," + maxValue + "]";
            throw new RuntimeException(error);
        }
        if (step > maxStep) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "步长不能超过" + maxStep + "V";
            throw new RuntimeException(error);
        }
    }

    /**
     * 检查signal的名字和值是否正确
     *
     * @param signals   信号
     * @param messages  消息集合
     * @param index     行号
     * @param className 类名
     */
    public void checkSignals(List<Pair<String, String>> signals, List<Message> messages, int index, String className) {
        for (Pair<String, String> pair : signals) {
            String signalName = pair.getFirst().trim();
            String value = pair.getSecond();
            Message message = getMessage(messages, signalName);
            if (message == null) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，找不到信号[" + signalName + "]";
                throw new RuntimeException(error);
            }
            Signal signal = getSignal(message, signalName);
            if (null == signal) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，CAN矩阵表中找不到" + signalName + "信号";
                throw new RuntimeException(error);
            } else {
                try {
                    checkCanValue(index, className, signalName, signal.getSignalSize(), ConvertUtils.convertLong(value));
                } catch (NumberFormatException e) {
                    String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，信号值填写错误[" + e.getMessage() + "]";
                    // throw new RuntimeException(error);
                    // 此处抛出异常，无法区分总线值和物理值
                    log.debug(error);

                }
            }
        }
    }


    /**
     * 检查Message ID的值是否正确
     *
     * @param messages  消息集合
     * @param index     行号
     * @param className 类名
     */
    public void checkExpectMessage(String signalName, Long expectValue, List<Message> messages, int index, String className) {
        Message message = getMessage(messages, signalName);
        if (null == message) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "CAN的信号名称[" + signalName + "]找不到";
            throw new RuntimeException(error);
        } else {
            Signal signal = null;
            for (Signal sig : message.getSignals()) {
                if (sig.getName().equals(signalName)) {
                    signal = sig;
                }
            }
            if (null == signal) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                        "CAN矩阵表中信号[" + message.getId() + "]找不到[" + signalName + "]信号";
                throw new RuntimeException(error);
            }
            checkCanValue(index, className, signalName, signal.getSignalSize(), expectValue);
        }
    }

    /**
     * 检查图片对比中的相似度是否正确
     *
     * @param similarity 相似度
     * @param index      行号
     * @param className  类名
     */
    public void checkSimilarity(Float similarity, int index, String className) {
        if (similarity < 0 || similarity > 100) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "相似度在0-100间， 当前值为" + similarity;
            throw new RuntimeException(error);
        }
    }

    /**
     * 检查图片对比中的相似度是否正确
     *
     * @param threshold 灰度二值化值
     * @param index     行号
     * @param className 类名
     */
    public void checkThreshold(Integer threshold, int index, String className) {
        if (threshold < 0 || threshold > 255) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "相似度在0-255间， 当前值为" + threshold;
            throw new RuntimeException(error);
        }
    }

    /**
     * 检查定义的element是否能够找到
     *
     * @param elementsName 其他表定义的element集合
     * @param index        行号
     * @param className    类名
     * @param elements     Sheet【element】读取出来内容
     */
    public void checkElementsExist(List<String> elementsName, int index, String className, List<BaseEntity> elements) {
        for (String elementName : elementsName) {
            checkElementExist(elementName, index, className, elements);
        }
    }


    /**
     * 检查定义的element是否能够找到
     *
     * @param elementName 其他表中定义的element
     * @param index       行号
     * @param className   类名
     * @param elements    Sheet【element】读取出来内容
     */
    public void checkElementExist(String elementName, int index, String className, List<BaseEntity> elements) {
        boolean flag = false;
        for (BaseEntity baseEntity : elements) {
            Element element = (Element) baseEntity;
            if (element.getName().equalsIgnoreCase(elementName)) {
                flag = true;
                break;
            }
        }
        if (!flag) {
            String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据填写错误，" +
                    "" + elementName + "在Element表格中找不到";
            throw new RuntimeException(error);
        }
    }


    /**
     * 查找重复的函数名
     *
     * @param entities  实体清单
     * @param className 类名
     */
    public void findDuplicate(List<BaseEntity> entities, String className) {
        Map<String, BaseEntity> map = new HashMap<>(12);
        for (int i = 0; i < entities.size(); i++) {
            int index = i + 1;
            BaseEntity baseEntity = entities.get(i);
            String name = baseEntity.getName();
            if (map.containsKey(baseEntity.getName())) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据" + name + "有重复，请检查";
                throw new RuntimeException(error);
            } else {
                map.put(name, baseEntity);
            }
        }
    }

    /**
     * 查找重复的函数名
     *
     * @param entities  实体清单
     * @param className 类名
     */
    public void findImageNameDuplicate(List<BaseEntity> entities, String className) {
        Map<String, BaseEntity> map = new HashMap<>(12);
        for (int i = 0; i < entities.size(); i++) {
            int index = i + 1;
            ScreenShotAction screenShotAction = (ScreenShotAction) entities.get(i);
            String name = screenShotAction.getImageName();
            if (map.containsKey(screenShotAction.getImageName())) {
                String error = "Sheet[" + CharUtils.upperCase(className) + "]的第" + index + "行数据" + name + "有重复，请检查";
                throw new RuntimeException(error);
            } else {
                map.put(name, screenShotAction);
            }
        }
    }

    /**
     * 检查测试用例中的执行部分，即BatteryAction=battery_test1
     *
     * @param pairs 前置条件/操作步骤/期望结果的部分
     * @param index 序号
     * @param map   所有Sheet的集合
     */
    public void checkAction(List<Pair<TestCaseFunctionTypeEnum, String>> pairs, int index, Map<String, List<BaseEntity>> map) {
        for (Pair<TestCaseFunctionTypeEnum, String> pair : pairs) {
            TestCaseFunctionTypeEnum typeEnum = pair.getFirst();
            // 函数名，需要做处理
            String functionName = pair.getSecond();
            if (!StringsUtils.isEmpty(functionName)) {
                functionName = functionName.trim().replace(" ", "_")
                        .replace("-", "_");
            }
            if (!(typeEnum == TestCaseFunctionTypeEnum.SLEEP || typeEnum == TestCaseFunctionTypeEnum.YIELD
                    || typeEnum == TestCaseFunctionTypeEnum.CLEAR || typeEnum == TestCaseFunctionTypeEnum.PASS
                    || typeEnum == TestCaseFunctionTypeEnum.STACK || typeEnum == TestCaseFunctionTypeEnum.LOST
                    || typeEnum == TestCaseFunctionTypeEnum.OPEN || typeEnum == TestCaseFunctionTypeEnum.CLOSE)) {
                List<BaseEntity> entities = map.get((CharUtils.lowerCase(typeEnum.getValue())));
                boolean flag = false;
                for (BaseEntity baseEntity : entities) {
                    String entityName = baseEntity.getName();
                    log.debug("entityName is {}", entityName);
                    if (entityName.equalsIgnoreCase(functionName)) {
                        flag = true;
                        break;
                    }
                }
                if (!flag) {
                    String error = "Sheet[TestCase]的第" + index + "行数据在[" + CharUtils.upperCase(typeEnum.getValue()) +
                            "]中找不到方法" + functionName;
                    throw new RuntimeException(error);
                }
            }
        }
    }

    /**
     * 检查测试用例前置条件的模块是否在测试用例模块中能找到
     *
     * @param moduleName 模块名
     * @param index      序号
     * @param className  类名
     * @param entities   实体清单
     */
    public void checkModule(String moduleName, int index, String className, List<BaseEntity> entities) {
        boolean flag = false;
        for (BaseEntity baseEntity : entities) {
            TestCase testCase = (TestCase) baseEntity;
            // 函数名，需要做处理
            if (testCase.getModuleName().equalsIgnoreCase(moduleName)) {
                flag = true;
                break;
            }
        }
        if (!flag) {
            String error = "Sheet[" + className + "]的第" + index + "行的类型" + moduleName + "在TestCase中找不到";
            throw new RuntimeException(error);

        }
    }

    /**
     * 检查要保存的信息是否在Information中能找到
     *
     * @param informationCompare 函数名
     * @param index              序号
     * @param className          类名
     * @param entities           实体清单
     */
    public void checkInformation(InformationCompare informationCompare, int index, String className, List<BaseEntity> entities) {
        String info = informationCompare.getInfo();
        String origin = informationCompare.getSavedInformation();
        if (StringsUtils.isNotEmpty(info) && StringsUtils.isNotEmpty(origin)) {
            String error = "Sheet[" + className + "]的第" + index + "行的中既填写了属性信息info[" + info + "]，又填写了保存的信息savedInformation[" + origin + "]";
            throw new RuntimeException(error);
        }
        if (StringsUtils.isNotEmpty(origin)) {
            boolean flag = false;
            for (BaseEntity baseEntity : entities) {
                Information information = (Information) baseEntity;
                if (origin.equalsIgnoreCase(information.getName())) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                String error = "Sheet[" + className + "]的第" + index + "行的原始信息[" + origin + "]在Information中找不到";
                throw new RuntimeException(error);
            }
        }
    }

    /**
     * 检查elements的数量是否符合element的操作
     *
     * @param elementAction element操作
     * @param index         序号
     * @param className     类名
     */
    public void checkElementOperation(ElementAction elementAction, int index, String className) {
        ElementOperationTypeEnum type = elementAction.getOperationActionType();
        int size = elementAction.getElements().size();
        int slideTimes = elementAction.getSlideTimes();
        if (type.getValue().contains("滑")) {
            if (size != 2) {
                String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作元素必须等于2个";
                throw new RuntimeException(error);
            }
            if (type == ElementOperationTypeEnum.SLIDE_RIGHT || type == ElementOperationTypeEnum.SLIDE_LEFT
                    || type == ElementOperationTypeEnum.SLIDE_UP || type == ElementOperationTypeEnum.SLIDE_DOWN) {
                if (slideTimes == 0) {
                    String error = "Sheet[" + className + "]的第" + index + "行的滑动次数必须大于0";
                    throw new RuntimeException(error);
                }
            }
        } else if (type == ElementOperationTypeEnum.PRESS) {
            if (size != 1) {
                String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作元素必须等于1个";
                throw new RuntimeException(error);
            }
            if (slideTimes == 0) {
                String error = "Sheet[" + className + "]的第" + index + "行的长按时间必须大于0";
                throw new RuntimeException(error);
            }
        } else {
            if (size != 1) {
                String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作元素必须等于1个";
                throw new RuntimeException(error);
            }
        }
    }

    /**
     * 检查操作是否合规
     *
     * @param screenOpsAction 操作
     * @param index           序号
     * @param className       类名
     */
    public void checkOpsType(ScreenOpsAction screenOpsAction, int index, String className) {
        ScreenOperationTypeEnum type = screenOpsAction.getScreenOperationType();
        DeviceTpeEnum opsType = screenOpsAction.getDeviceType();
        List<Pair<Integer, Integer>> points = screenOpsAction.getPoints();
        double continueTime = screenOpsAction.getContinueTimes();
        // ANDROID只支持点击以及拖动
        // QNX不支持拖动
        if (opsType == DeviceTpeEnum.ANDROID) {
            if (!(type == ScreenOperationTypeEnum.DRAG || type == ScreenOperationTypeEnum.CLICK)) {
                String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作设备仅支持Qnx设备";
                throw new RuntimeException(error);
            }
            if (type == ScreenOperationTypeEnum.DRAG) {
                if (points.size() != 2) {
                    String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作坐标点必须为2组";
                    throw new RuntimeException(error);
                }
            }
            if (type == ScreenOperationTypeEnum.CLICK) {
                if (points.size() != 1) {
                    String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作坐标点必须为1组";
                    throw new RuntimeException(error);
                }
            }
        } else {
            if (type == ScreenOperationTypeEnum.DRAG) {
                String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作设备仅支持QNX设备";
                throw new RuntimeException(error);
            }
            if (type == ScreenOperationTypeEnum.CLICK) {
                if (points.size() != 1) {
                    String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作坐标点必须为1组";
                    throw new RuntimeException(error);
                }
            } else {
                if (type == ScreenOperationTypeEnum.SLIDE) {
                    if (points.size() != 2) {
                        String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作坐标点必须为2组";
                        throw new RuntimeException(error);
                    }
                    if (continueTime <= 0) {
                        String error = "Sheet[" + className + "]的第" + index + "行的操作持续时间填写不正确";
                        throw new RuntimeException(error);
                    }
                } else {
                    if (points.size() != 1) {
                        String error = "Sheet[" + className + "]的第" + index + "行的操作为" + type.getValue() + "，该操作坐标点必须为1组";
                        throw new RuntimeException(error);
                    }
                    if (type == ScreenOperationTypeEnum.PRESS) {
                        if (continueTime <= 0) {
                            String error = "Sheet[" + className + "]的第" + index + "行的操作持续时间填写不正确";
                            throw new RuntimeException(error);
                        }
                    }
                }
            }
        }

    }


    /**
     * 检查是否符合规则
     * 1、必须有一个yield
     * 2、yield前面必须要有一个函数，哪怕是pass
     * 3、yield后面必须要有一个函数，哪怕是pass
     *
     * @param pairs     测试用例前置条件
     * @param index     序号
     * @param className 类名
     */
    public void checkRule(List<Pair<TestCaseFunctionTypeEnum, String>> pairs, int index, String className) {
        boolean flag = false;
        int size = pairs.size();
        int yeildIndex = -1;
        for (int i = 0; i < size; i++) {
            Pair<TestCaseFunctionTypeEnum, String> pair = pairs.get(i);
            if (pair.getFirst() == TestCaseFunctionTypeEnum.YIELD) {
                flag = true;
                yeildIndex = i;
                if (i == 0 || i == size - 1) {
                    String error = "Sheet[" + className + "]的第" + index + "行执行条件不正确，YIELD前后必须要有函数";
                    throw new RuntimeException(error);
                }
            }
        }
        if (!flag) {
            String error = "Sheet[" + className + "]的第" + index + "行执行条件不正确，必须要包含一个YIELD";
            throw new RuntimeException(error);
        }
        boolean passFlag = false;
        // 检查前面的部分
        for (int i = 0; i < yeildIndex; i++) {
            Pair<TestCaseFunctionTypeEnum, String> pair = pairs.get(i);
            if (pair.getFirst() == TestCaseFunctionTypeEnum.PASS) {
                passFlag = true;
            }
        }
        if (yeildIndex > 1 && passFlag) {
            String error = "Sheet[" + className + "]的第" + index + "行执行条件不正确，前半部分不能既有PASS，又有函数";
            throw new RuntimeException(error);
        }
        passFlag = false;
        // 检查后面的部分
        for (int i = yeildIndex + 1; i < size; i++) {
            Pair<TestCaseFunctionTypeEnum, String> pair = pairs.get(i);
            if (pair.getFirst() == TestCaseFunctionTypeEnum.PASS) {
                passFlag = true;
            }
        }
        if (size - yeildIndex > 2 && passFlag) {
            String error = "Sheet[" + className + "]的第" + index + "行执行条件不正确，后半部分不能既有PASS，又有函数";
            throw new RuntimeException(error);
        }
    }

    /**
     * 此处必须以=号分割的来表示参数名和参数值
     *
     * @param params    参数名列表
     * @param index     序号
     * @param className 类名
     */
    public void checkParam(List<String> params, int index, String className) {
        for (String param : params) {
            if (param.split(EQUAL).length != 2) {
                String error = "Sheet[" + className + "]的第" + index + "行函数参数不正确，必须有函数的参数名和参数值，并以=号分开，" +
                        "如file=\"aaa\" 或者 value={\"aa\": \"bb\"}";
                throw new RuntimeException(error);
            }
        }


    }
}
