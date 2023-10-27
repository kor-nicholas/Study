package com.study.mygenerateid.idgenerators;

import com.study.IdGenerator;
import com.study.mygenerateid.entities.SKU;
import org.springframework.stereotype.Component;

@Component
public class SKUIdGenerator implements IdGenerator<SKU> {

    @Override
    public SKU generate() {
        return new SKU("sku");
    }
}
