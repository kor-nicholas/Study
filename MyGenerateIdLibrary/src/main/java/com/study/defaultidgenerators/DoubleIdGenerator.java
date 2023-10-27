package com.study.defaultidgenerators;

import com.study.IdGenerator;
import org.springframework.stereotype.Service;

import java.util.Random;

@Service
public class DoubleIdGenerator implements IdGenerator<Double> {
    @Override
    public Double generate() {
        var random = new Random();
        var result = random.nextDouble();
        return result;
    }
}