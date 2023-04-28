package com.study.StudySpringBoot.students;

import jakarta.websocket.server.PathParam;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("student")
public class StudentController {
    private final StudentService studentService;

    public StudentController(StudentService studentService) {
        this.studentService = studentService;
    }

    @GetMapping(path = "list")
    public List<Student> list() {
        return studentService.list();
    }

    // curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"John Doe\", \"birthday\": \"1998-05-10\"}" http://localhost:8080/add
    @PostMapping(path = "add")
    // use json-object in body
    public void add(@RequestBody Student student) {
        studentService.add(student);
    }

    // curl -X DELETE -H "Content-Type: application/json" http://localhost:8080/student/delete/3
    @DeleteMapping(path = "delete/{id}")
    public void delete(@PathVariable int id) {
        studentService.delete(id);
    }

    // curl -X PUT -H "Content-Type: application/json" -d "{\"id\": 4, \"name\": \"Alex Lastname\"}" http://localhost:8080/student/change
    // curl -X PUT -H "Content-Type: application/json" -d "{\"id\": 5, \"birthday\": \"1934-02-03\"}" http://localhost:8080/student/change
    // curl -X PUT -H "Content-Type: application/json" -d "{\"id\": 1, \"name\": \"Katya Petrushka\", \"birthday\": \"2005-05-10\"}" http://localhost:8080/student/change
    @PutMapping(path = "change")
    public void change(@RequestBody Student student) {
        studentService.change(student);
    }
}
