package com.philosophy.base.util;

import com.philosophy.BaseTestUtils;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static org.junit.jupiter.api.Assertions.*;

class FilesUtilsTest {


    private static final String RESOURCES = BaseTestUtils.getResourceFolder();

    @Test
    void getCurrentPath() {
        String str = FilesUtils.getCurrentPath();
        String currentPath = "D:\\Workspace\\sophia";
        assertEquals(currentPath, str);
    }

    @Test
    void size() throws IOException {
        Path file = Paths.get(RESOURCES + "\\1.jpg");
        long size = FilesUtils.size(file);
        assertEquals(size, 1718);
        Path folder = Paths.get(RESOURCES + "\\Downloads");
        long folderSize = FilesUtils.size(folder);
        assertEquals(folderSize,5143 );
    }

    @Test
    void getExtension() throws IOException {
        Path file = Paths.get(RESOURCES + "1.jpg");
        assertEquals("jpg",FilesUtils.getExtension(file));
    }

    @Test
    void deleteFiles() throws IOException {
        Path file1 = Paths.get(RESOURCES + "\\1.txt");
        Path file2 = Paths.get(RESOURCES + "\\2.txt");
        Path file3 = Paths.get(RESOURCES + "\\3.txt");
        Path file4 = Paths.get(RESOURCES + "\\4.txt");
        Files.createFile(file1);
        Files.createFile(file2);
        Files.createFile(file3);
        Files.createFile(file4);
        assertTrue(Files.exists(file1));
        assertTrue(Files.exists(file2));
        assertTrue(Files.exists(file3));
        assertTrue(Files.exists(file4));
        FilesUtils.deleteFiles(file1, file2,file3,file4);
        assertFalse(Files.exists(file1));
        assertFalse(Files.exists(file2));
        assertFalse(Files.exists(file3));
        assertFalse(Files.exists(file4));
    }
}