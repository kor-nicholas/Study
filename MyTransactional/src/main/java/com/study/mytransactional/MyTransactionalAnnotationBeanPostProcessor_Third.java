package com.study.mytransactional;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanPostProcessor;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class MyTransactionalAnnotationBeanPostProcessor_Third implements BeanPostProcessor {
    Logger logger = Logger.getLogger(String.valueOf(MyTransactionalAnnotationBeanPostProcessor_Third.class));
    private List<Method> list = new ArrayList<>();

    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        var methods = bean.getClass().getDeclaredMethods();
        for (var method : methods) {
            if (method.isAnnotationPresent(MyTransactional.class)) {
                list.add(method);
                logger.info("add: " + method.getName());
            }
        }
        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        if (!list.isEmpty()) {
            logger.info("get: " + String.valueOf(list));

            // TODO: proxy all methods from list
            return Proxy.newProxyInstance(
                    bean.getClass().getClassLoader(),
                    bean.getClass().getInterfaces(),
                    new InvocationHandler() {
                        @Override
                        public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                            System.out.println("before invoke method");
                            logger.info("before invoke method");
                            list.clear();
                            return proxy;
                        }
                    }
            );
        }
        return bean;
    }
}
