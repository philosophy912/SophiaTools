package com.chinatsp.code.checker.impl.collection;

import com.chinatsp.code.checker.api.BaseChecker;
import com.chinatsp.code.checker.api.IChecker;
import com.chinatsp.code.configure.Configure;
import com.chinatsp.code.entity.BaseEntity;
import com.chinatsp.code.entity.collection.Can;
import com.chinatsp.dbc.entity.Message;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;

@Component
@Slf4j
public class CanChecker extends BaseChecker implements IChecker {

    @Override
    public void check(Map<String, List<BaseEntity>> map, List<Message> messages, Configure configure) {
        List<BaseEntity> entities = getEntity(map, Can.class);
        for (int i = 0; i < entities.size(); i++) {
            int index = i + 1;
            Can can = (Can) entities.get(i);
            String name = can.getClass().getSimpleName();
            // 检查名字是否符合python命名规范
            checkUtils.checkPythonFunction(can.getName(), index, name);
            // 检查CAN的Signals的信号和值是否符合要求
            checkUtils.checkSignals(can.getSignals(), messages, index, name);
        }
        // 检查函数名是否有重名
        checkUtils.findDuplicate(entities, Can.class.getSimpleName());
    }
}
