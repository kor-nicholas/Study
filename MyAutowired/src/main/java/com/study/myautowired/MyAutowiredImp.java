package com.study.myautowired;

import java.lang.reflect.Field;
import java.util.Arrays;

public class MyAutowiredImp {
    public static void process(Object object) throws IllegalAccessException {
        Class<?> clas = object.getClass();
        Arrays.stream(clas.getDeclaredFields())
                .filter(field -> field.isAnnotationPresent(MyAutowired.class))
                .forEach(field -> injectField(object, field));
    }

    private static void injectField(Object object, Field field) {
        try {
            Class<?> type = field.getType();
            Object dependency = type.newInstance();
            field.setAccessible(true);
            field.set(object, dependency);
        } catch (InstantiationException | IllegalAccessException e) {
            e.printStackTrace();
        }
    }
}
