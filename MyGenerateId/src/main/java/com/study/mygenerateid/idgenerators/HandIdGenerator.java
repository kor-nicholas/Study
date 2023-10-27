package com.study.mygenerateid.idgenerators;

import com.study.IdGenerator;
import com.study.mygenerateid.entities.Hand;
import org.springframework.stereotype.Component;

@Component
public class HandIdGenerator implements IdGenerator<Hand> {
    @Override
    public Hand generate() {
        return new Hand("you will be magic", 10);
    }
}
