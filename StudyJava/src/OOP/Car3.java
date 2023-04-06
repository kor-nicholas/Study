package OOP;

public class Car3 extends Transport3 {
    public Car3(float speed, float weight, String color, byte[] coordinate) {
        super(speed, weight, color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
    }

    // abstract method which we realization
    @Override
    public void moveObject(float speed) {
        System.out.println("Object moved " + speed + " per hour");
    }

}
