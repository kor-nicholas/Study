package com.study.mytransactional;

import org.springframework.stereotype.Service;

import java.util.Random;

@Service
public class MySecondService implements MyInterfaces {
    @MyTransactional
    @Override
    public void voidMethod() {
        System.out.println("MySecondService:Void method...");
    }

    @MyTransactional
    @Override
    public String stringMethod() {
        System.out.println("MySecondService:String method...");
        return "MySecondService:String method...";
    }

    @MyTransactional
    @Override
    public int intMethod() {
        Random random = new Random();
        int number = random.nextInt();
        System.out.printf("MySecondService:Int method with %s number", number);
        return number;
    }

    @Override
    public boolean booleanMethod() {
        Random random = new Random();
        boolean bool = random.nextBoolean();
        System.out.printf("MySecondService:Boolean method with %s boolean-value", bool);
        return bool;
    }
}
