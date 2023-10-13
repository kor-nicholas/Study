package com.study.mytransactional;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Component;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

@Component
public class MyTransactionalAnnotationBeanPostProcessor_Second implements BeanPostProcessor {
    @Autowired
    private ApplicationContext context;

    private ConfigurableListableBeanFactory factory;
    @Autowired
    private List<Method> methodsToProxy = new ArrayList<>();
    Logger logger = Logger.getLogger(String.valueOf(MyTransactionalAnnotationBeanPostProcessor_Second.class));
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        Method[] methods = bean.getClass().getDeclaredMethods();
        for (Method method: methods) {
            if (method.isAnnotationPresent(MyTransactional.class)) {
                methodsToProxy.add(method);
                logger.info("add");
            }
        }
        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        if (methodsToProxy.isEmpty()) {
            logger.info("get");
            methodsToProxy.clear();
        }




//        if (beanName.equals("myService")) {
//            var methods = bean.getClass().getDeclaredMethods();
//            for (var method : methods) {
//                var annotation = method.getAnnotation(MyTransactional.class);
//                if (annotation != null) {
//                    logger.info("Yes");
//                    System.out.println("Yes");
//                    ProxyFactory proxyFactory = new ProxyFactory(bean);
//                    proxyFactory.setProxyTargetClass(true);
//
//                    proxyFactory.addAdvice(new MethodInterceptor() {
//                        @Override
//                        public Object invoke(MethodInvocation invocation) throws Throwable {
//                            // TODO: before and after invoke method
//                            logger.info("before/after invoke method");
//                            return invocation.proceed();
//                        }
//                    });
//                    var proxy = proxyFactory.getProxy();
//                    return proxy;
//                }
//            }
//        }

        return bean;
    }
}
