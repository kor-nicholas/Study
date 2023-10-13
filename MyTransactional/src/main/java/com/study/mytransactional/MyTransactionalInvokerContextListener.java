package com.study.mytransactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationListener;
import org.springframework.context.event.ContextRefreshedEvent;
import org.springframework.stereotype.Component;
import org.springframework.transaction.PlatformTransactionManager;

import java.lang.reflect.Method;
import java.util.logging.Logger;

//@Component
//public class MyTransactionalInvokerContextListener implements ApplicationListener<ContextRefreshedEvent> {
//    public MyTransactionalInvokerContextListener(){
//
//    }
//    @Autowired
//    PlatformTransactionManager transactionManager;
//    private ConfigurableListableBeanFactory factory;
//    private Logger logger = Logger.getLogger(String.valueOf(MyTransactionalInvokerContextListener.class));
//
//    @Override
//    public void onApplicationEvent(ContextRefreshedEvent event) {
//        ApplicationContext context = event.getApplicationContext();
//        factory = (ConfigurableListableBeanFactory) context.getAutowireCapableBeanFactory();
//
//        String[] names = context.getBeanDefinitionNames();
//        for (String name: names) {
//            BeanDefinition beanDefinition = factory.getBeanDefinition(name);
//            String originalClassName = beanDefinition.getBeanClassName();
//            try {
//                Class<?> originalClass = Class.forName(originalClassName);
//                Method[] methods = originalClass.getMethods();
//                for (Method method: methods) {
//                    if (method.isAnnotationPresent(MyTransactional.class)) {
//                        Object bean = context.getBean(name);
//                        Method currentMethod = bean.getClass().getMethod(method.getName(), method.getParameterTypes());
//                        currentMethod.invoke(bean);
//                    }
//                }
//            } catch (Exception e) {
//                e.printStackTrace();
//            }
//        }
//    }
//}
