package com.study.mytransactional;

import org.springframework.cglib.proxy.MethodInterceptor;
import org.springframework.cglib.proxy.MethodProxy;

import java.lang.reflect.Method;
import java.util.logging.Logger;

public class MyMethodInterceptor implements MethodInterceptor {
    Logger logger = Logger.getLogger(String.valueOf(MethodInterceptor.class));
    @Override
    public Object intercept(Object obj, Method method, Object[] args, MethodProxy proxy) throws Throwable {
        // TODO: Before invoke method
        logger.info("Before invoke method");

        Object result = proxy.invoke(obj, args);

        // TODO: After invoke method
        logger.info("After invoke method");

        return result;
    }
}
