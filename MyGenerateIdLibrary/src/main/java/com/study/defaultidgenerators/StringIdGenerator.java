package com.study.defaultidgenerators;

import com.study.IdGenerator;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class StringIdGenerator implements IdGenerator<String> {
    @Override
    public String generate() {
        var result = UUID.randomUUID().toString();
        return result;
    }
}
