package OOP;

public class Transport5 {
    private float speed, weight;
    protected String color;
    private byte[] coordinate;

    // Default constructor
    public Transport5() {
        this.speed = 0.0f;
        this.weight = 0.0f;
        this.color = "white";
        this.coordinate = new byte[] {0, 0, 0};
    }

    public Transport5(String color, byte[] coordinate) {
        this.color = color;
        this.coordinate = coordinate;
    }

    public Transport5(float speed, float weight, String color, byte[] coordinate) {
        this.speed = speed;
        this.weight = weight;
        this.color = color;
        this.coordinate = coordinate;
    }

    public String getValues() {
        return "Speed: " + this.speed + " | Weight: " + this.weight + " | Color: " + this.color + " | Coordinate: " + this.coordinate[0] + "." + this.coordinate[1] + "." + this.coordinate[2];
    }

    // Inside class
    public class Engine {
        private boolean isReady;
        private int km;

        public Engine(boolean isReady, int km) {
            this.isReady = isReady;
            this.km = km;
        }

        public void Info() {
            if(isReady) {
                System.out.println("Engine ready for work");
            } else {
                System.out.println("Engine doesn't ready for work. It complete " + km + " km.");
            }
        }
    }
}
