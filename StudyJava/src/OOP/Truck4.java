package OOP;

public class Truck4 extends Transport4 {
    // Field for Inside class
    public Engine engine = new Engine(false, 100000);
    private boolean isLoaded;
    public Truck4(String color, byte[] coordinate) {
        super(color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
    }

    public Truck4(String color, byte[] coordinate, boolean isLoaded) {
        super(color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
        this.isLoaded = isLoaded;
    }

    @Override
    public String getValues() {
        return super.getValues() + " | isLoaded: " + isLoaded;
    }
}
