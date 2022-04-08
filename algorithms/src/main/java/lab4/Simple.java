/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package knu.fit.ist.ta2.lab4;

/**
 *
 * @author ProBook
 */
public class Simple {
    private String text = "What Industries Can Benefit from IoT? \n" +
"Organizations best suited for IoT are those that would benefit from using sensor devices in their business processes. \n" +
"\n" +
"Manufacturing \n" +
"Manufacturers can gain a competitive advantage by using production-line monitoring to enable proactive maintenance on equipment when sensors detect an impending failure. Sensors can actually measure when production output is compromised. With the help of sensor alerts, manufacturers can quickly check equipment for accuracy or remove it from production until it is repaired. This allows companies to reduce operating costs, get better uptime, and improve asset performance management. \n" +
"\n" +
"Automotive \n" +
"The automotive industry stands to realize significant advantages from the use of IoT applications. In addition to the benefits of applying IoT to production lines, sensors can detect impending equipment failure in vehicles already on the road and can alert the driver with details and recommendations. Thanks to aggregated information gathered by IoT-based applications, automotive manufacturers and suppliers can learn more about how to keep cars running and car owners informed. \n" +
"\n" +
"Transportation and Logistics \n" +
"Transportation and logistical systems benefit from a variety of IoT applications. Fleets of cars, trucks, ships, and trains that carry inventory can be rerouted based on weather conditions, vehicle availability, or driver availability, thanks to IoT sensor data. The inventory itself could also be equipped with sensors for track-and-trace and temperature-control monitoring. The food and beverage, flower, and pharmaceutical industries often carry temperature-sensitive inventory that would benefit greatly from IoT monitoring applications that send alerts when temperatures rise or fall to a level that threatens the product. \n" +
"\n" +
"Retail \n" +
"IoT applications allow retail companies to manage inventory, improve customer experience, optimize supply chain, and reduce operational costs. For example, smart shelves fitted with weight sensors can collect RFID-based information and send the data to the IoT platform to automatically monitor inventory and trigger alerts if items are running low. Beacons can push targeted offers and promotions to customers to provide an engaging experience. \n" +
"\n" +
"Public Sector \n" +
"The benefits of IoT in the public sector and other service-related environments are similarly wide-ranging. For example, government-owned utilities can use IoT-based applications to notify their users of mass outages and even of smaller interruptions of water, power, or sewer services. IoT applications can collect data concerning the scope of an outage and deploy resources to help utilities recover from outages with greater speed. \n" +
"\n" +
"Healthcare \n" +
"IoT asset monitoring provides multiple benefits to the healthcare industry. Doctors, nurses, and orderlies often need to know the exact location of patient-assistance assets such as wheelchairs. When a hospital’s wheelchairs are equipped with IoT sensors, they can be tracked from the IoT asset-monitoring application so that anyone looking for one can quickly find the nearest available wheelchair. Many hospital assets can be tracked this way to ensure proper usage as well as financial accounting for the physical assets in each department. \n" +
"\n" +
"General Safety Across All Industries \n" +
"In addition to tracking physical assets, IoT can be used to improve worker safety. Employees in hazardous environments such as mines, oil and gas fields, and chemical and power plants, for example, need to know about the occurrence of a hazardous event that might affect them. When they are connected to IoT sensor–based applications, they can be notified of accidents or rescued from them as swiftly as possible. IoT applications are also used for wearables that can monitor human health and environmental conditions. Not only do these types of applications help people better understand their own health, they also permit physicians to monitor patients remotely.";
    private String clearText = changeText();
    private final String[] words = clearText.split(" ");
    StringProcessing sp = new StringProcessing(clearText);
    Demo demo = new Demo();
    
    public String getText () {
        return text;
    }
    
    private String changeText () {
        String local_text = text;
        local_text = local_text.replaceAll("[?\n,.]","").trim().toLowerCase();
        
        return local_text;
    }
    
    public String task1 () {
        // Очищений текст :
        
        return clearText;
    }
    
    public int task2 () {
        // Загальна кiлькiсть слiв у текстi :
        
        int count = 0;
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') {
                count++;
            }
        }
        
        return count;
    }
    
    public int task3 () {
        // Кiлькiсть унiкальних слiв у текстi :
        
        int count = 0;        
        for (int i = 0, j = 0; i < changeText().length();i++) {
            if (changeText().charAt(i) == ' ') {
                if (changeText().indexOf(changeText().substring(j,i),i+1) == -1)
                    count++;
                j = i + 1;
            }
        }
        
        return count;
    }
    
    public String task4 () {
        // Визначити перші 3 слова, що зустрічаються найчастіше
        
        demo.calculateResult(sp.getList(sp.getText()));
        String local_text = demo.getResultList().toString();
        local_text = "[" + local_text.substring(8,25) + " ; " + local_text.substring(35,53) + " ; " + local_text.substring(63,81) + "]";
        
        return local_text;
    }
    
    public int task5 () {
        // Визначити кількість слів що не містять літеру b
        
        int count = 0;
        for (int i = 0; i < words.length;i++) {
            if (words[i].indexOf('b') == -1) {
                count++;
            }
        }

        return count;
    }
    
    public int task6 () {
        // Визначити кількість слів, що мають рівно 3 літери
        
        int count = 0;
        for (int i = 0; i < words.length;i++) {
            if (words[i].length() == 3) 
                count++;
        }

        return count;
    }
    
    public String task7 () {
        // Визначити перші 8 трьохлітерні послідовності у словах тексту, що зустрічаються найчастіше
        
        demo.calculateResult(sp.getSet(sp.getText()), 3);
        String local_text = demo.getResultList().toString();
        local_text = "[" + local_text.substring(8,26) + " ; " + local_text.substring(36,54) + " ; " + local_text.substring(64,82) +
                " ; " + local_text.substring(92,109) + " ; " + local_text.substring(119,136) + " ; " + local_text.substring(146,163) +
                " ; " + local_text.substring(173,190) + " ; " + local_text.substring(200,217) + "]";
        
        return local_text;
        
    }
    
    /*public static void main(String[] args) {
    Simple simple = new Simple();
    
    System.out.println(simple.task2());
    System.out.println(simple.task3());
    System.out.println(simple.task5());
    System.out.println(simple.task6());
    }*/
}
