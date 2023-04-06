package OOP;

public class Car extends Transport2 {
    public Car(float speed, float weight, String color, byte[] coordinate) {
        super(speed, weight, color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
    }
}
