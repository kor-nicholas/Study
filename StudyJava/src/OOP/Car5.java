package OOP;

public class Car5 extends Transport5 {
    public static int count;
    // Field for Inside class
    public Engine engine = new Engine(true, 1000);
    public Car5(float speed, float weight, String color, byte[] coordinate) {
        super(speed, weight, color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
        count++;
    }

    public static int getCount() {
        return count;
    }

    public void turnOn() {
        System.out.println("All devices in car turned on");
    }

    public void turnOn(int countOfDevices) {
        System.out.println(countOfDevices + " devices in car turned on");
    }

    public void turnOn(String device) {
        System.out.println(device + " turned in the Car");
    }

    public void moveObject(float speed) {
        System.out.println("Object moved " + speed + " per hour");
    }
}
