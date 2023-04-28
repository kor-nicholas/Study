package com.study.StudySpringBoot.students;

import com.study.StudySpringBoot.responce.RestApiException;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class StudentService {
    private final Log _logger = LogFactory.getLog(StudentService.class);
    private final StudentRepository studentRepository;

    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    public List<Student> list() {
        return studentRepository.findAll();
    }

    public void add(Student student) {
        if(studentRepository.findStudentByEmail(student.getEmail()).isPresent()) {
            throw new RestApiException("Email is busy");
        }
        studentRepository.save(student);
    }

    public void delete(int id) {
        studentRepository.deleteById(id);
    }

    public void change(Student student) {
        Optional<Student> itemInBase = studentRepository.findById(student.getId());
        if(itemInBase.isPresent()) {
            Student item = itemInBase.get();

            if(student.getName() != null) {
                item.setName(student.getName());
            }

            if(student.getBirthday() != null) {
                item.setBirthday(student.getBirthday());
            }

            studentRepository.save(item);
        }
    }
}
