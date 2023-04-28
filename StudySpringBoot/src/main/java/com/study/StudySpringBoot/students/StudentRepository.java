package com.study.StudySpringBoot.students;

import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;

public interface StudentRepository extends JpaRepository<Student, Integer> {

    Optional<Student> findStudentByEmail(String email);
}
