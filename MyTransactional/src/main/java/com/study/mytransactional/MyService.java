package com.study.mytransactional;

import org.springframework.stereotype.Service;

import java.util.Random;

@MyTransactional
@Service
public class MyService implements MyInterfaces {
    @Override
    public void voidMethod() {
        System.out.println("MyService:Void method...");
    }

    @Override
    public String stringMethod() {
        System.out.println("MyService:String method...");
        return "MyService:String method...";
    }

    @Override
    public int intMethod() {
        Random random = new Random();
        int number = random.nextInt();
        System.out.printf("MyService:Int method with %s number", number);
        return number;
    }

    @Override
    public boolean booleanMethod() {
        Random random = new Random();
        boolean bool = random.nextBoolean();
        System.out.printf("MyService:Boolean method with %s boolean-value", bool);
        return bool;
    }
}
