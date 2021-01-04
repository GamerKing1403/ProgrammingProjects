import java.util.Scanner;

public class EncoderandDecoder {

    final static String CODER = "thequickbrownfoxjumpsoverthelazydog", CODER_INT = "AFTERSHOCK";

    static Scanner sc1 = new Scanner(System.in);

    public static void main(String[] args) {

        char ch2 = 'y';
        while (ch2 == 'y' || ch2 == 'Y') {
            System.out.println("Do You Want To Encode Or Decode??");
            String eOrD = sc1.next();
            switch(eOrD){
                case "Encode":case "encode":
                    encoder();
                case "Decode":case "decode":
                    decoder();
                default:
                    System.out.println("Please enter One Of Those");
                    ch2 = 'Y';
            }
        }
    }

    public static void encoder() {
        System.out.println("Please Enter the Text:- ");
        String input = sc1.nextLine().toLowerCase();
        String output = "";
        for (int i = 0; i < input.length(); i++) {
            char in = input.charAt(i);
            if (Character.isAlphabetic(in)) {
                output += CODER.indexOf(in) + 1 + " ";
            } else if (Character.isDigit(in)) {
                output += CODER_INT.charAt(Integer.valueOf(Character.toString(in))) + " ";
            } else if (in == 32) {
                output += ". ";
            } else {
                output += Character.toString(in);
            }
        }
        System.out.println(output);
        System.out.println("Do Your Want to Continue???????????");

    }

    public static void decoder() {

        System.out.println("Please Enter the Encoded Text:- ");
        String input = sc1.nextLine();
        String output = "";
        if (input.lastIndexOf(" ") != input.length() - 1) {
            input += " ";
        }
        boolean charecter = false;
        for (int i = 0; i < input.length() - 1; i += input.indexOf(" ") + 1) {
            String in = input.substring(i, input.indexOf(" ") + i);
            int output_int = 0;
            try {
                output_int = Integer.parseInt(in);
            } catch (NumberFormatException e) {
                charecter = true;
            }
            if (charecter) {
                if (CODER_INT.contains(in)) {
                    output += CODER_INT.indexOf(in);
                } else if (in.equals(".")) {
                    output += " ";
                } else {
                    output += in;
                }
            } else {
                output += CODER.charAt(output_int - 1);
            }
        }
        System.out.println(output);
        System.out.println("Do Your Want to Continue???????????");

    }
}
