package com.chinatsp.code.writer;

import com.chinatsp.code.BaseTestUtils;
import com.chinatsp.code.entity.BaseEntity;
import com.chinatsp.code.enumeration.ConfigureTypeEnum;
import com.chinatsp.code.service.api.IReadService;
import com.chinatsp.code.writer.api.TestCaseFreeMarkers;
import com.chinatsp.code.writer.impl.testcase.TestCaseWriter;
import com.philosophy.base.common.Pair;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Map;

/**
 * @author lizhe
 * @date 2020/9/28 11:21
 **/
@RunWith(SpringRunner.class)
@SpringBootTest
@Slf4j
class WriterTest {

    @Autowired
    private IReadService readerService;
    @Autowired
    private FreeMarkerWriter freeMarkerWriter;
    @Autowired
    private TestCaseWriter testCaseWriter;

    private Map<ConfigureTypeEnum, String> map;

    private Map<String, List<BaseEntity>> entities;

    @BeforeEach
    void beforeTest() {
        Path path = Paths.get(BaseTestUtils.getFileFolder(), "template.xlsx");
        Pair<Map<String, List<BaseEntity>>, Map<ConfigureTypeEnum, String>> content = readerService.read(path);
        map = content.getSecond();
        entities = content.getFirst();
    }


    @Test
    void writeConfigure() {
        Path path = Paths.get(BaseTestUtils.getCodeFolder(), "configure.py");
        freeMarkerWriter.writeConfigure(map, path);
    }

    @Test
    void writeEntity() {
        Path path = Paths.get(BaseTestUtils.getCodeFolder(), "context.py");
        freeMarkerWriter.writeEntity(entities, path);
    }

    @Test
    void writeTestCase() {
        Map<String, TestCaseFreeMarkers> map = testCaseWriter.convert(entities);
        for (Map.Entry<String, TestCaseFreeMarkers> entry : map.entrySet()) {
            String key = entry.getKey();
            TestCaseFreeMarkers freeMarker = entry.getValue();
            Path path = Paths.get(BaseTestUtils.getCodeFolder(), "test_" + key + ".py");
            freeMarkerWriter.writeTestCase(freeMarker, path);
        }

    }

}