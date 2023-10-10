package com.study.myautowired;

import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class Test {

    @MyAutowired(required = false)
    Product product;

//    @Autowired
//    public Test(Product product) {
//        this.product = product;
//        System.out.println("product = " + product);
//    }

    @PostConstruct
    public void test() {
        System.out.println("product.getId() = " + product.getId());
    }
}
