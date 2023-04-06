package OOP;

public class Transport2 {
    private float speed, weight;
    protected String color;
    private byte[] coordinate;

    // Default constructor
    public Transport2() {
        this.speed = 0.0f;
        this.weight = 0.0f;
        this.color = "white";
        this.coordinate = new byte[] {0, 0, 0};
    }

    public Transport2(String color, byte[] coordinate) {
        this.color = color;
        this.coordinate = coordinate;
    }

    public Transport2(float speed, float weight, String color, byte[] coordinate) {
        this.speed = speed;
        this.weight = weight;
        this.color = color;
        this.coordinate = coordinate;
    }

    public String getValues() {
        return "Speed: " + this.speed + " | Weight: " + this.weight + " | Color: " + this.color + " | Coordinate: " + this.coordinate[0] + "." + this.coordinate[1] + "." + this.coordinate[2];
    }
}
