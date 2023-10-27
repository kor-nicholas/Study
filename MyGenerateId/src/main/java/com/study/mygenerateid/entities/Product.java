package com.study.mygenerateid.entities;

import com.study.MyGenerateId;
import org.springframework.stereotype.Component;

@Component
public class Product {
    @MyGenerateId
    private SKU sku;

    public SKU getSku() {
        return sku;
    }
}
