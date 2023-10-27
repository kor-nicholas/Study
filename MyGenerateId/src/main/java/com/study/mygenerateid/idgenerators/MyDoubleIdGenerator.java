package com.study.mygenerateid.idgenerators;

import java.text.DecimalFormat;
import java.util.Random;

import com.study.defaultidgenerators.DoubleIdGenerator;
import org.springframework.stereotype.Component;

@Component
public class MyDoubleIdGenerator extends DoubleIdGenerator {
    @Override
    public Double generate() {
        var random = new Random();
        var result = roundDouble(random.nextDouble(1, 150), 2);
        return result;
    }

    private double roundDouble(double value, int countNumbersAfterPoint) {
        DecimalFormat df = new DecimalFormat("#." + "#".repeat(countNumbersAfterPoint));
        return Double.valueOf(df.format(value));
    }
}
