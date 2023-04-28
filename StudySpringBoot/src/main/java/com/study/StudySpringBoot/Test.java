package com.study.StudySpringBoot;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// https://localhost:5432/test
@RestController
@RequestMapping("test")
public class Test {
    // https://localhost:5432/test/helloWorld
    @GetMapping(path = "helloWorld")
    public String helloWorld() {
        return "Hello World!";
    }
}
