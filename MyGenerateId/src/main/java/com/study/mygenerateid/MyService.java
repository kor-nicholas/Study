package com.study.mygenerateid;

import com.study.mygenerateid.entities.Hand;
import com.study.mygenerateid.entities.Person;
import com.study.mygenerateid.entities.Product;
import com.study.mygenerateid.entities.SKU;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class MyService implements MyInterface {

    @Autowired
    Person person;

    @Autowired
    Product product;
    @Override
    public int getIntId() {
        return person.getIntId();
    }

    @Override
    public double getDoubleId() {
        return person.getDoubleId();
    }

    @Override
    public String getStringId() {
        return person.getStringId();
    }

    @Override
    public UUID getUuidId() {
        return person.getUuidId();
    }

    @Override
    public Hand getHandId() {
        return person.getHandId();
    }

    @Override
    public SKU getSkuId() {
        return product.getSku();
    }
}
