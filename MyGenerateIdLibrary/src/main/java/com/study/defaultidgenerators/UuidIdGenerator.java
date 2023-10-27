package com.study.defaultidgenerators;

import com.study.IdGenerator;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class UuidIdGenerator implements IdGenerator<UUID> {
    @Override
    public UUID generate() {
        var result = UUID.randomUUID();
        return result;
    }
}
