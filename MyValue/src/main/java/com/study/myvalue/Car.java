package com.study.myvalue;

import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.util.logging.Logger;

@Component
public class Car {
    private int id;
    @Value("Mercedes-Benz")
    private String brand;
    @MyValue("${app.model}")
    private String model;
    @MyValue("${app.capacityEngine}")
    private String capacityEngine;

    @PostConstruct
    public void showData(){
        Logger.getLogger(String.valueOf(Car.class)).info("Brand: " + brand + " | Model: " + model + " | Capacity Engine: " + capacityEngine);
    }

    @Override
    public String toString() {
        return "Car{" +
                "id=" + id +
                ", brand='" + brand + '\'' +
                ", model='" + model + '\'' +
                ", capacityEngine=" + capacityEngine +
                '}';
    }
}
