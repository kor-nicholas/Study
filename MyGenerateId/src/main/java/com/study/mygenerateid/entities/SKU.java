package com.study.mygenerateid.entities;

import org.springframework.stereotype.Component;

@Component
public class SKU {
    private String value;

    public SKU() {
    }

    public SKU(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }

    @Override
    public String toString() {
        return "SKU{" +
                "value='" + value + '\'' +
                '}';
    }
}
