package OOP;

public abstract class Transport3 {
    private float speed, weight;
    protected String color;
    private byte[] coordinate;

    // Default constructor
    public Transport3() {
        this.speed = 0.0f;
        this.weight = 0.0f;
        this.color = "white";
        this.coordinate = new byte[] {0, 0, 0};
    }

    public Transport3(String color, byte[] coordinate) {
        this.color = color;
        this.coordinate = coordinate;
    }

    public Transport3(float speed, float weight, String color, byte[] coordinate) {
        this.speed = speed;
        this.weight = weight;
        this.color = color;
        this.coordinate = coordinate;
    }

    // abstract method which we will need to realization (like interface)
    public abstract void moveObject(float speed);

    public String getValues() {
        return "Speed: " + this.speed + " | Weight: " + this.weight + " | Color: " + this.color + " | Coordinate: " + this.coordinate[0] + "." + this.coordinate[1] + "." + this.coordinate[2];
    }
}
