package com.study.mytransactional;

import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

import java.util.logging.Logger;

@Aspect
@Component
public class MyAspect {
    Logger logger = Logger.getLogger(String.valueOf(MyAspect.class));

    @Before("@annotation(com.study.mytransactional.MyTransactional)")
    public void beforeMyTransactionalMethod() {
        logger.info("My Aspect working...");
        System.out.println("My Aspect...");
    }
}
