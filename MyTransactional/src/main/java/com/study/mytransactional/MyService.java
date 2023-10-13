package com.study.mytransactional;

import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@MyTransactional
public class MyService {
    public MyService() {

    }
    @PostConstruct
    @Transactional
    public void performTransactionalOperation_First() {
        // TODO: transaction...
        System.out.println("Transactional First...");
    }

    @PostConstruct
    @MyTransactional
    private void performTransactionalOperation_Second() {
        // TODO: transaction...
        System.out.println("MyTransaction Second...");
    }

    @PostConstruct
    @MyTransactional
    private void performanceTransactionOperation_Third() {
        // TODO: transaction...
        System.out.println("MyTransaction Third...");
    }
}
