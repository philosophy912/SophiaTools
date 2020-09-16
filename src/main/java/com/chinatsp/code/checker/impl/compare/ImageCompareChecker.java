package com.chinatsp.code.checker.impl.compare;

import com.chinatsp.code.checker.api.BaseChecker;
import com.chinatsp.code.checker.api.IChecker;
import com.chinatsp.code.configure.Configure;
import com.chinatsp.code.entity.BaseEntity;
import com.chinatsp.code.entity.actions.ScreenShotAction;
import com.chinatsp.code.entity.compare.ImageCompare;
import com.chinatsp.dbc.entity.Message;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;

@Component
public class ImageCompareChecker extends BaseChecker implements IChecker {


    @Override
    public void check(Map<String, List<BaseEntity>> map, List<Message> messages, Configure configure) {
        List<BaseEntity> entities = getEntity(map, ImageCompare.class);
        int maxWidth = configure.getMaxWidth();
        int maxHeight = configure.getMaxHeight();
        for (int i = 0; i < entities.size(); i++) {
            int index = i + 1;
            ImageCompare imageCompare = (ImageCompare) entities.get(i);
            String name = imageCompare.getClass().getSimpleName();
            // 检查名字是否符合python命名规范
            checkUtils.checkPythonFunction(imageCompare.getName(), index, name);
            // 检查图片是否符合要求
            checkUtils.checkScreenshotName(imageCompare.getImageName(), index, name);
            // 检查相似度
            checkUtils.checkSimilarity(imageCompare.getSimilarity(), index, name);
            // 检查灰度二值化值
            checkUtils.checkThreshold(imageCompare.getThreshold(), index, name);
            // 检查比较区域
            checkUtils.checkClickPositions(imageCompare.getPositions(), index, name, maxWidth, maxHeight);
            // 检查模板图片
            checkUtils.checkTemplateImage(imageCompare.getTemplateDark(), index, name);
            checkUtils.checkTemplateImage(imageCompare.getTemplateLight(), index, name);
        }
        // 检查函数名是否有重名
        checkUtils.findDuplicate(entities, ImageCompare.class.getSimpleName());
    }
}
