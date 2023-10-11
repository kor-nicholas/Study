package com.study.myautowired;

import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.util.Arrays;

@Component
public class Person {
    private int id;
    private String name;
//    @MyAutowired(required = false)
    private Product product1;
    @MyAutowired
    private void setProduct(Product product) {
        this.product1 = product;
    }

    @PostConstruct
    private void showData() {
        System.out.println("id = " + id);
        System.out.println("name = " + name);
        System.out.println("product = " + product1.getId());
        product1.setId(123);
    }
}
