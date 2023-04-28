package com.study.StudySpringBoot.students;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.time.Month;
import java.util.List;

@Configuration
public class StudentConfiguration {

    // add 2 students in database before start project
//    @Bean
//    public CommandLineRunner commandLineRunner(StudentRepository studentRepository) {
//        return args -> {
//            studentRepository.saveAll(List.of(
//                    new Student("Alex", LocalDate.of(2000, Month.JANUARY, 1)),
//                    new Student("Tom", LocalDate.of(2002, Month.FEBRUARY, 3))
//            ));
//        };
//    }
}
