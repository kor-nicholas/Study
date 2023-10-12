package com.study.myvalue;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.stereotype.Component;
import org.springframework.util.ReflectionUtils;
import org.springframework.util.ResourceUtils;

import java.io.*;
import java.util.Properties;
import java.util.UnknownFormatConversionException;
import java.util.logging.Logger;

@Component
public class MyValueAnnotationBeanPostProcessor implements BeanPostProcessor {
    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        var fields = bean.getClass().getDeclaredFields();
        for (var field : fields) {
            var annotation = field.getAnnotation(MyValue.class);
            if (annotation != null) {
                var value = annotation.value();
                if (value.contains("$") && value.contains("{") && value.contains("}")) {
                    Properties properties = new Properties();

                    try (InputStream in = new FileInputStream(ResourceUtils.getFile("classpath:application.properties"))) {
                        properties.load(in);
                        value = properties.getProperty(value.substring(2, value.length() - 1));
                    } catch (FileNotFoundException e) {
                        throw new UncheckedIOException("File not found", e);
                    } catch (IOException e) {
                        throw new UnknownFormatConversionException("Properties can't load");
                    }
                }
                field.setAccessible(true);
                ReflectionUtils.setField(field, bean, value);
            }
        }
        return bean;
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        return bean;
    }
}
