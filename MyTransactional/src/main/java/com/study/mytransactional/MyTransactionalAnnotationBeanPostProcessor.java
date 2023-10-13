package com.study.mytransactional;

import jakarta.annotation.Resource;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.cglib.proxy.Enhancer;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.stereotype.Component;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.TransactionManager;
import org.springframework.transaction.reactive.TransactionContextManager;
import org.springframework.transaction.support.TransactionTemplate;

import javax.sql.DataSource;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Logger;

//@Component
//public class MyTransactionalAnnotationBeanPostProcessor implements BeanPostProcessor {
//    @Autowired
//    PlatformTransactionManager transactionManager;
//    private Logger logger = Logger.getLogger(String.valueOf(MyTransactionalAnnotationBeanPostProcessor.class));
//    private Map<String, Class<?>> map = new HashMap<>();
//    @Override
//    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
//        var methods = bean.getClass().getDeclaredMethods();
//        for (var method: methods) {
////            if (method.isAnnotationPresent(MyTransactional.class)) {
////                logger.info("put: " +  beanName);
////                map.put(beanName, bean.getClass());
////            }
//        }
//
//        if (bean.getClass().isAnnotationPresent(MyTransactional.class)) {
//            map.put(beanName, bean.getClass());
//        }
//
//        return bean;
//    }
//
//    @Override
//    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
//        Class beanClass = map.get(beanName);
//        if (beanClass != null && beanName.equals("myService")) {
//            return Proxy.newProxyInstance(beanClass.getClass().getClassLoader(), beanClass.getClass().getInterfaces(), new InvocationHandler() {
//                @Override
//                public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
//                    logger.info("Method: " + method.getName());
//                    return method.invoke(bean, args);
//                }
//            });
//        }
//
////        if (beanName.contains("myService")) {
////            Enhancer enhacher = new Enhancer();
////            enhacher.setSuperclass(bean.getClass());
////            enhacher.setCallback(new MyMethodInterceptor());
////            return enhacher.create();
////        }
//
//        return bean;
//    }
//}
