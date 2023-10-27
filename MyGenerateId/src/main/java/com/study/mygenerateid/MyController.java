package com.study.mygenerateid;

import com.study.mygenerateid.entities.Hand;
import com.study.mygenerateid.entities.SKU;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.UUID;

@RestController
@Slf4j
public class MyController {

    @Autowired
    MyInterface myService;

    @GetMapping("getIntId")
    public int getIntId() {
        return myService.getIntId();
    }

    @GetMapping("getDoubleId")
    public double getDoubleId() {
        return myService.getDoubleId();
    }

    @GetMapping("getStringId")
    public String getStringId() {
        return myService.getStringId();
    }

    @GetMapping("getUuid")
    public UUID getUuid() {
        return myService.getUuidId();
    }

    @GetMapping("getHandId")
    public Hand getHandId() {
        return myService.getHandId();
    }

    @GetMapping("getSkuId")
    public SKU getSkuId() {
        return myService.getSkuId();
    }
}
