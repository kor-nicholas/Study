package com.study.mytransactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyController {
    @Autowired
    MyInterfaces myService;

    @Autowired
    MyInterfaces mySecondService;

    @GetMapping("myService/testVoid")
    public void myServiceTestVoid() {
        myService.voidMethod();
    }

    @GetMapping("mySecondService/testVoid")
    public void mySecondServiceTestVoid() {
        mySecondService.voidMethod();
    }

    @GetMapping("myService/testString")
    public String myServiceTestString() {
        return myService.stringMethod();
    }

    @GetMapping("mySecondService/testString")
    public String mySecondServiceTestString() {
        return mySecondService.stringMethod();
    }

    @GetMapping("myService/testInt")
    public int myServiceTestInt() {
        return myService.intMethod();
    }

    @GetMapping("mySecondService/testInt")
    public int mySecondServiceTestInt() {
        return mySecondService.intMethod();
    }

    @GetMapping("myService/testBoolean")
    public boolean myServiceTestBoolean() {
        return myService.booleanMethod();
    }

    @GetMapping("mySecondService/testBoolean")
    public boolean mySecondServiceTestBoolean() {
        return mySecondService.booleanMethod();
    }
}
