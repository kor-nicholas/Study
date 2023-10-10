package com.study.myautowired;

import org.springframework.stereotype.Component;

@Component
public class Product {
    public void setId(int id) {
        this.id = id;
    }

    private int id = 456;

    public Product() {
    }

    public int getId() {
        return id;
    }
}
