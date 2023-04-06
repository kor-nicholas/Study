package OOP;

public class Car6 extends Transport5 implements ILight {
    public static int count;
    private boolean isOn;
    // Field for Inside class
    public Engine engine = new Engine(true, 1000);
    public Car6(float speed, float weight, String color, byte[] coordinate) {
        super(speed, weight, color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
        count++;
    }

    public Car6() {}

    @Override
    public void setLight(boolean set) {
        this.isOn = set;
    }

    @Override
    public void blinkLight() {
        System.out.println("Blink light");
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
