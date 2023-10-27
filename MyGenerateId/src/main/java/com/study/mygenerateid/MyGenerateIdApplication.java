package com.study.mygenerateid;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan(basePackages = "com.study")
public class MyGenerateIdApplication {

    public static void main(String[] args) {
        SpringApplication.run(MyGenerateIdApplication.class, args);
    }

}
