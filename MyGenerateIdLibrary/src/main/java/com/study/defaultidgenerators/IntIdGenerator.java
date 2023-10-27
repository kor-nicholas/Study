package com.study.defaultidgenerators;

import com.study.IdGenerator;
import org.springframework.stereotype.Service;

import java.util.Random;

@Service
public class IntIdGenerator implements IdGenerator<Integer> {
    @Override
    public Integer generate() {
        var random = new Random();
        var result = random.nextInt();
        return result;
    }
}
