package com.chinatsp.code.checker.impl.testcase;

import com.chinatsp.code.checker.api.BaseChecker;
import com.chinatsp.code.checker.api.IChecker;
import com.chinatsp.code.entity.BaseEntity;
import com.chinatsp.code.entity.storage.Information;
import com.chinatsp.code.entity.testcase.TestCase;
import com.chinatsp.code.entity.testcase.TestCaseSetUp;
import com.chinatsp.code.enumeration.ConfigureTypeEnum;
import com.chinatsp.dbc.entity.Message;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;

/**
 * @author lizhe
 * @date 2020/9/16 10:51
 **/
@Component
@Slf4j
public class TestCaseSetUpChecker extends BaseChecker implements IChecker {

    @Override
    public void check(Map<String, List<BaseEntity>> map, List<Message> messages, Map<ConfigureTypeEnum, String> configure) {
        List<BaseEntity> entities = getEntity(map, TestCaseSetUp.class);
        List<BaseEntity> testCaseEntities = getEntity(map, TestCase.class);
        for (int i = 0; i < entities.size(); i++) {
            int index = i + 1;
            TestCaseSetUp testCaseSetUp = (TestCaseSetUp) entities.get(i);
            String name = testCaseSetUp.getClass().getSimpleName();
            // 检查名字是否符合python命名规范
            checkUtils.checkModule(testCaseSetUp.getName(), index, name, testCaseEntities);
            //检查module是否有重复
            checkUtils.findDuplicate(entities, TestCaseSetUp.class.getSimpleName());
            //检查module中是否符合规范
            checkUtils.checkRule(testCaseSetUp.getSuites(), index, name);
            checkUtils.checkRule(testCaseSetUp.getFunctions(), index, name);
            //检查module中是否有相关的函数
            log.debug("检查module中是否有相关的函数");
            checkUtils.checkAction(testCaseSetUp.getSuites(), index, map);
            checkUtils.checkAction(testCaseSetUp.getFunctions(), index, map);
        }
    }
}
