package OOP;

public class Car4 extends Transport4 {
    // Field for Inside class
    public Engine engine = new Engine(true, 1000);
    public Car4(float speed, float weight, String color, byte[] coordinate) {
        super(speed, weight, color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
    }

    public void moveObject(float speed) {
        System.out.println("Object moved " + speed + " per hour");
    }
}
