package OOP;

public class Transport1 {
    // public - allow everywhere
    // protected - allow only in this class and childs
    // private - close, use only in this class

    public float speed, weight;
    public String color;
    public byte[] coordinate;

    public void setValues(float _speed, float _weight, String _color, byte[] _coordinate) {
        speed = _speed;
        weight = _weight;
        color = _color;
        coordinate = _coordinate;
    }

    public String getValues() {
        return "Speed: " + speed + " | Weight: " + weight + " | Color: " + color + " | Coordinate: " + coordinate[0] + "." + coordinate[1] + "." + coordinate[2];
    }
}
