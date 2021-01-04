
package Main;
import java.util.Scanner;
import java.util.ArrayList;

public class Decoder {

    private static final Scanner SCANNER = new Scanner(System.in);
    private static String text_to_decode;
    private static String in;
    private static String output = "";
    private static final String CODER_INT="AFTERSHOCK", CODER="thequickbrownfoxjumpsoverthelazydog";
    private static final ArrayList<Integer> INDICES = new ArrayList<>();
    private static boolean character=false;
    private static int output_int = 0;
	
    public static void main(String[] args) {

        try (SCANNER) {
            Decoder();
        }

    }

    private static void Decoder() {

            // Inputs.
            System.out.println("The Text to Decode :-");
            text_to_decode = SCANNER.nextLine();

            // Getting all the indices of all the space in the Input.
            for(int i = 0; i < text_to_decode.length();i++) {
                    if(text_to_decode.charAt(i) == ' ') {
                            INDICES.add(i);
                    }
            }

            // Main loop
            for (int i : INDICES) {

                try {
                    if(i == INDICES.get(0)) {
                            in = text_to_decode.substring(0, i);
                    }else {
                            try {
                                    in = text_to_decode.substring(INDICES.get(INDICES.indexOf(i) - 1), i);
                            }catch(IndexOutOfBoundsException e) {
                                    in = text_to_decode.substring(i, text_to_decode.length());
                            }
                    }
                } catch (IndexOutOfBoundsException e){
                    System.out.println(e.getMessage());
                    break;
                }

                try {
                    in = in.trim();
                    output_int = Integer.parseInt(in);
                } catch (NumberFormatException e) {
                    character = true;
                }

                if (character) {
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
                System.out.println(1);
                character = false;
            }

        System.out.println("The coded Text was:- " + output);
    }

}
