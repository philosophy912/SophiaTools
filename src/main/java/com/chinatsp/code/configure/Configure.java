package com.chinatsp.code.configure;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

/**
 * @author lizhe
 * @date 2020/9/11 15:32
 **/
@Setter
@Getter
@ToString
public class Configure {
    /**
     * 最大支持的显示屏的个数
     */
    private Integer maxDisplay;
    /**
     * 最大支持的电压值
     */
    private Double maxVoltage;
    /**
     * 最大支持的继电器通道
     */
    private Integer maxRelayChannel;
    /**
     * 最小支持的电压值
     */
    private Double minVoltage;
    /**
     * SOC串口号
     */
    private String socPort;
    /**
     * SOC串口波特率
     */
    private Integer socBaudRate;
    /**
     * MCU串口号
     */
    private String mcuPort;
    /**
     * MCU串口波特率
     */
    private String mcuBaudRate;
    /**
     * 显示屏宽
     */
    private Integer maxWidth;
    /**
     * 显示屏高
     */
    private Integer maxHeight;
    /**
     * 临时图片存放路径
     */
    private String screenShotTempPath;
    /**
     * 模板图片存放路径
     */
    private String templateImagePath;
    /**
     * CAN的DBC文件绝对路径
     */
    private String dbcFile;
    /**
     * CAN的dbc文件转换成json文件
     */
    private String dbcJson;

}
