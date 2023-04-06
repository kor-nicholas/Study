package OOP;

public class Main {
    public static void main(String[] args) {
        // Theory for OOP:
        // Encapsulation: field must be private
        // Inheritance (nasledovanie): create child
        // Polymorphizm: rewrite method for child
        // Abstract class(interface): no create object, template for method

        // -----------------------------------------------------------------
        // Public, Protected, Private (Transport1)

        Transport1 bmv = new Transport1();
        bmv.setValues(200.0f, 2500.0f, "black", new byte[] {0, 0, 0});
//        bmv.speed = 200.0f;
//        bmv.weight = 2500.0f;
//        bmv.color = "black";
//        bmv.coordinate = new byte[] {0, 0, 0};
        System.out.println("BMV\n" + bmv.getValues());
        // [output] BMV
        // [output] Speed: 200.0 | Weight: 2500.0 | Color: black | Coordinate: 0.0.0

        Transport1 mercedes = new Transport1();
        mercedes.speed = 300.0f;
        mercedes.weight = 1500.0f;
        mercedes.color = "black";
        mercedes.coordinate = new byte[] {50, 0, 0};
        System.out.println("Mercedes\n" + mercedes.getValues());
        // [output] Mercedes
        // [output] Speed: 300.0 | Weight: 1500.0 | Color: black | Coordinate: 50.0.0

        System.out.println("\nBMV vs Mercedes");
        System.out.println("Speed: " + bmv.speed + " | " + mercedes.speed);
        System.out.println("Weight: " + bmv.weight + " | " + mercedes.weight);
        System.out.println("Color: " + bmv.color + " | " + mercedes.color);
        System.out.println("Coordinate: " + bmv.coordinate[0] + "." + bmv.coordinate[1] + "." + bmv.coordinate[2] + " | " + mercedes.coordinate[0] + "." + mercedes.coordinate[1] + "." + mercedes.coordinate[2]);
        // [output] BMV vs Mercedes
        // [output] Speed: 200.0 | 300.0
        // [output] Weight: 2500.0 | 1500.0
        // [output] Color: black | black
        // [output] Coordinate: 0.0.0 | 50.0.0

        // -----------------------------------------------------------------
        // Constructors (Transport2)

        Transport2 alfaRomeo = new Transport2(400.0f, 1000.0f, "red", new byte[] {100, 0, 0});
        System.out.println("\nAlfa-Romeo");
        System.out.println(alfaRomeo.getValues());
        // [output] Alfa-Romeo
        // [output] Speed: 400.0 | Weight: 1000.0 | Color: red | Coordinate: 100.0.0

        Transport2 mazda = new Transport2("green", new byte[] {10, 0, 0});
        System.out.println("\nMazda");
        System.out.println(mazda.getValues());
        // [output] Mazda
        // [output] Speed: 0.0 | Weight: 0.0 | Color: green | Coordinate: 10.0.0

        // -----------------------------------------------------------------
        // Inheritance (Car | Truck)

        Car alfaRomeo2 = new Car(400.0f, 1000.0f, "red", new byte[] {100, 0, 0});
        System.out.println("\nAlfa-Romeo2");
        System.out.println(alfaRomeo2.getValues());
        // [output] Alfa-Romeo2
        // [output] Speed: 400.0 | Weight: 1000.0 | Color: red | Coordinate: 100.0.0

        Truck kamaz = new Truck("green", new byte[] {10, 0, 0}, false);
        kamaz.setLoaded(true);
        System.out.println("\nKamaz");
        System.out.println("Loaded: " + kamaz.getLoaded());
        // [output] Kamaz
        // [output] Truck is loaded
        // [output] Loaded: true

        // -----------------------------------------------------------------
        // Polymorphizm (Truck2)

        Truck2 kamaz2 = new Truck2("green", new byte[] {10, 0, 0}, false);
        System.out.println("\nKamaz2");
        System.out.println(kamaz2.getValues());
        // [output] Kamaz2
        // [output] Speed: 0.0 | Weight: 0.0 | Color: green | Coordinate: 10.0.0 | isLoaded: false

        Transport2 mazda2 = new Transport2("green", new byte[] {10, 0, 0});
        System.out.println("\nMazda2");
        System.out.println(mazda2.getValues());
        // [output] Mazda2
        // [output] Speed: 0.0 | Weight: 0.0 | Color: green | Coordinate: 10.0.0

        // -----------------------------------------------------------------
        // Abstract class and abstract method (Transport3, Truck3, Car3)

        Transport3 transport3 = new Car3(400.0f, 1000.0f, "red", new byte[] {100, 0, 0});
        transport3 = new Truck3("red", new byte[] {100, 0, 0});

        System.out.println();
        transport3.moveObject(100.0f);
        // [output] Object moved 100.0 per hour

        // -----------------------------------------------------------------
        // Inside and anonymous class (Transport4, Truck4, Car4)

        Transport4 truck4 = new Truck4("blue", new byte[] {70, 0, 0});
        Car4 car4 = new Car4(220, 1500, "yellow", new byte[] {30, 0, 0});

        System.out.println();

        // use Inside class
        ((Truck4) truck4).engine.Info();
        // [output] Engine doesn't ready for work. It complete 100000 km.
        car4.engine.Info();
        // [output] Engine ready for work

        // use Anonymous class, Override only for this object
        Car4 flyCar = new Car4(220, 1500, "yellow", new byte[] {30, 0, 0}) {
            @Override
            public void moveObject(float speed) {
                super.moveObject(speed);
                System.out.println("But it's Fly Car ;)");
            }
        };

        flyCar.moveObject(500);
        // [output] Object moved 500.0 per hour
        // [output] But it's Fly Car ;)

        // -----------------------------------------------------------------
        // Packages, Overload(peregruzka), static + final (Transport5, Car5)

        // package - folder
        // import package.package.class to use class in class from other package

        // overload
        Car5 car5 = new Car5(220, 1500, "yellow", new byte[] {30, 0, 0});

        System.out.println();

        car5.turnOn("light");
        car5.turnOn(5);
        car5.turnOn();
        // [output] light turned in the Car
        // [output] 5 devices in car turned on
        // [output] All devices in car turned on

        // static - for class (method work only with static field and static method)
        Car5 car5_1 = new Car5(220, 1500, "yellow", new byte[] {30, 0, 0});
        Car5 car5_2 = new Car5(220, 1500, "yellow", new byte[] {30, 0, 0});
        Car5 car5_3 = new Car5(220, 1500, "yellow", new byte[] {30, 0, 0});

        System.out.println(Car5.count);
        System.out.println("Count of Car5: " + Car5.getCount());
        // [output] 4
        // [output] Count of Car5: 4

        // final - const (field, method, class)
        // final field -> must be value and we will can't change it
        // final method -> we will can't @Override
        // final class -> class will hasn't child
        // final + abstract class -> Error

        // -----------------------------------------------------------------
        // Interface (ILight, Car6)

        Car6 car6 = new Car6();

        System.out.println();

        car6.setLight(true);
        car6.blinkLight();
        // [output] Blink light
    }
}
