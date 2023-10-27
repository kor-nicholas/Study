package com.study.mygenerateid;

import com.study.mygenerateid.entities.Hand;
import com.study.mygenerateid.entities.SKU;

import java.util.UUID;

public interface MyInterface {
    int getIntId();
    double getDoubleId();
    String getStringId();
    UUID getUuidId();
    Hand getHandId();
    SKU getSkuId();
}
