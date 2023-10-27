package com.study;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.BeanInitializationException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.context.ApplicationContext;
import org.springframework.core.ResolvableType;
import org.springframework.stereotype.Component;
import org.springframework.util.ReflectionUtils;

import java.lang.reflect.InvocationTargetException;
import java.util.*;

@Component
@Slf4j
public class MyGenerateIdAnnotationBeanPostProcessor implements BeanPostProcessor {
    @Autowired
    private ApplicationContext context;

    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        var fields = bean.getClass().getDeclaredFields();
        for (var field : fields) {
            if (field.isAnnotationPresent(MyGenerateId.class)) {
                field.setAccessible(true);
                try {
                    var idGeneratorImplementations = context.getBeanNamesForType(ResolvableType.forClassWithGenerics(IdGenerator.class, field.getType()));
                    var implementation = context.getBean(idGeneratorImplementations[0]);
                    log.info(Arrays.toString(idGeneratorImplementations));

                    for (var method: IdGenerator.class.getMethods()) {
                        var implMethod = implementation.getClass().getMethod(method.getName());
                        implMethod.setAccessible(true);
                        var result = implMethod.invoke(implementation, null);
                        ReflectionUtils.setField(field, bean, result);
                    }
                } catch (BeansException | NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
                    throw new BeanInitializationException("Could not set value in field", e);
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
