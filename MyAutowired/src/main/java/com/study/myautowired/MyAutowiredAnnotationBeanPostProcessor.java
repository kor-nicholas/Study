package com.study.myautowired;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.BeanInitializationException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanFactoryPostProcessor;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Component;
import org.springframework.util.ReflectionUtils;

import java.lang.reflect.InvocationTargetException;
import java.lang.annotation.Annotation;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.logging.Logger;

@Component
public class MyAutowiredAnnotationBeanPostProcessor implements BeanPostProcessor {

    @Autowired
    ApplicationContext context;

    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        var fields = bean.getClass().getDeclaredFields();
        for (var field : fields) {
            var annotation = field.getAnnotation(MyAutowired.class);
            if (annotation != null) {
                field.setAccessible(true);
                try {
                    var beanForField = context.getBean(field.getType());
                    ReflectionUtils.setField(field, bean, beanForField);
                } catch (BeansException e) {
                    if (annotation.required()) {
                        throw new BeanInitializationException("Could not Autowire", e);
                    }
                }
            }
        }

        var methods = bean.getClass().getDeclaredMethods();
        for (var method : methods) {
            var annotation = method.getAnnotation(MyAutowired.class);
            if (annotation != null) {
                try {
                    var beanToInject = context.getBean(method.getParameterTypes()[0]);
                    method.setAccessible(true);
                    method.invoke(bean, beanToInject);
                } catch (Exception e) {
                    if (annotation.required()) {
                        throw new BeanInitializationException("Could not Autowire", e);
                    }
                }
            }
        }

        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        return bean;
    }
}
