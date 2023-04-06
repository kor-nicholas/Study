package OOP;

public class Truck3 extends Transport3 {
    private boolean isLoaded;
    public Truck3(String color, byte[] coordinate) {
        super(color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
    }

    public Truck3(String color, byte[] coordinate, boolean isLoaded) {
        super(color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
        this.isLoaded = isLoaded;
    }

    // abstract method which we realization
    @Override
    public void moveObject(float speed) {
        System.out.println("Object moved " + speed + " per hour");
    }

    @Override
    public String getValues() {
        return super.getValues() + " | isLoaded: " + isLoaded;
    }

    public void setLoaded(boolean loaded) {
        this.isLoaded = loaded;
    }

    public boolean getLoaded() {
        if(isLoaded) {
            System.out.println("Truck is loaded");
            return true;
        } else {
            System.out.println("Truck isn't loaded");
            return false;
        }
    }
}
