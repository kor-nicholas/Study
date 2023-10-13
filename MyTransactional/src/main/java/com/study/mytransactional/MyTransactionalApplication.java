package com.study.mytransactional;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@SpringBootApplication
@EnableTransactionManagement
@EnableAspectJAutoProxy
public class MyTransactionalApplication {

	public static void main(String[] args) {
		SpringApplication.run(MyTransactionalApplication.class, args);
	}

}
