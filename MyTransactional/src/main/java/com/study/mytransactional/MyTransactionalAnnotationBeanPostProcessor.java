package com.study.mytransactional;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.stereotype.Component;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.TransactionStatus;
import org.springframework.transaction.support.DefaultTransactionDefinition;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

@Component
@Slf4j
public class MyTransactionalAnnotationBeanPostProcessor implements BeanPostProcessor {
    @Autowired
    PlatformTransactionManager transactionManager;
    HashMap<String, Class> mapOfBean = new HashMap<>();
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        if (!mapOfBean.isEmpty()) {
            mapOfBean.clear();
        }

        var methods = bean.getClass().getDeclaredMethods();
        for (var method : methods) {
            if (method.isAnnotationPresent(MyTransactional.class) || bean.getClass().isAnnotationPresent(MyTransactional.class)) {
                mapOfBean.put(beanName, bean.getClass());
                return bean;
            }
        }

        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        Class beanClass = mapOfBean.get(beanName);
        if (beanClass != null) {
            return Proxy.newProxyInstance(
                    beanClass.getClassLoader(),
                    beanClass.getInterfaces(),
                    new InvocationHandler() {
                        @Override
                        public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                            Method realBeanMethod = beanClass.getDeclaredMethod(method.getName());
                            if (realBeanMethod.isAnnotationPresent(MyTransactional.class) || bean.getClass().isAnnotationPresent(MyTransactional.class)) {
                                log.info("Proxy method " + method.getName());
                                var definition = new DefaultTransactionDefinition();
                                var transaction = transactionManager.getTransaction(definition);
                                try {
                                    var result = method.invoke(bean, args);
                                    transactionManager.commit(transaction);
                                    return result;
                                } catch (Exception e) {
                                    transactionManager.rollback(transaction);
                                    throw e;
                                }
                            } else {
                                return method.invoke(bean, args);
                            }
                        }
                    }
            );
        }

        return bean;
    }
}
