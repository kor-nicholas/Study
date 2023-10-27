package com.study.mygenerateid.idgenerators;

import com.study.defaultidgenerators.IntIdGenerator;
import org.springframework.stereotype.Component;

@Component
public class MyIntIdGeneratorImp extends IntIdGenerator {
    @Override
    public Integer generate() {
        return 1402985345;
    }
}
