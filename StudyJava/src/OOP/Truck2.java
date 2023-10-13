package OOP;

public class Truck2 extends Transport2 {
    private boolean isLoaded;
    public Truck2(String color, byte[] coordinate) {
        super(color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
    }

    public Truck2(String color, byte[] coordinate, boolean isLoaded) {
        super(color, coordinate); // to constructor for parent
        super.color = color; // to field in parent
        this.isLoaded = isLoaded;
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