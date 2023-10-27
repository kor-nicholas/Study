package com.study.mygenerateid.entities;

import com.study.MyGenerateId;
import org.springframework.stereotype.Component;

import java.util.UUID;

@Component
public class Person {

    // TODO: find out to change int (now work only with Integer, because method is
    // generate<T> and we can't to give int
    @MyGenerateId
    private Integer intId;

    // TODO: with Double to double too
    @MyGenerateId
    private Double doubleId;

    @MyGenerateId
    private String stringId;

    @MyGenerateId
    private UUID uuidId;

    @MyGenerateId
    private Hand handId;

    public int getIntId() {
        return intId;
    }

    public double getDoubleId() {
        return doubleId;
    }

    public String getStringId() {
        return stringId;
    }

    public UUID getUuidId() {
        return uuidId;
    }

    public Hand getHandId() {
        return handId;
    }
}
