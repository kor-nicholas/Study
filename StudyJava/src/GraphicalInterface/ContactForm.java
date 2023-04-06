package GraphicalInterface;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ContactForm extends JFrame {
    JTextField nameField, emailField;
    JRadioButton male, female;
    JCheckBox checkBox;
    public ContactForm() {
        // title - name for window, top
        super("Contact Form");
        // x, y - from top-left, width, height - for window
        super.setBounds(200, 100, 300, 230);
        // close app if click for Close
        super.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // container - our container for objects which works in app
        Container container = super.getContentPane();
        // how objects locate
        container.setLayout(new GridLayout(5, 2, 2, 10));

        JLabel name = new JLabel("Enter name: ");
        nameField = new JTextField("name", 1);
        JLabel email = new JLabel("Enter email: ");
        emailField = new JTextField("email", 1);

        container.add(name);
        container.add(nameField);
        container.add(email);
        container.add(emailField);

        male = new JRadioButton("Male");
        female = new JRadioButton("Female");
        checkBox = new JCheckBox("Are you agree with Rules?", true);
        JButton sendButton = new JButton("Send");

        // firstly select male
        male.setSelected(true);
        container.add(male);
        container.add(female);
        ButtonGroup group = new ButtonGroup();
        group.add(male);
        group.add(female);

        container.add(checkBox);
        container.add(sendButton);

        sendButton.addActionListener(new ButtonEventManager());
    }

    public class ButtonEventManager implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            // text from fields that entered user
            String name = nameField.getText();
            String email = emailField.getText();

            String isMale = "Male";
            if(!male.isSelected()) {
                isMale = "Female";
            }

            boolean check_box = checkBox.isSelected();

            JOptionPane.showMessageDialog(null,
                    "Your data:\n\nEmail: " + email + "\nMale/Female: " + isMale + "\nAre you agree?: " + check_box,
                    "Hello " + name,
                    JOptionPane.PLAIN_MESSAGE);
        }
    }
}
