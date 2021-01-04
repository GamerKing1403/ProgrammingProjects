package decipher;

import java.util.Random;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class game1 {
	
	private static Random rand = new Random();
	private static final String[] codes = {"THIS IS A SECRET CODE","HELLO WORLD","WELCOME USER","MUMMA","PAPA","CHERRY","TUSHKI"
			,"GUI","JAVA","PYTHON"};
	private static final String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ";
	private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static String coded_txt, output;

	public static void main(String[] args) throws java.io.IOException {

		int key = 5;
		
		int randint = rand.nextInt(10);
		coded_txt = codes[randint];
		output="";
		
		for(char ch : coded_txt.toCharArray()) {
			if(ch != ' ') {
				output += alpha.charAt(alpha.indexOf(ch) + key);
			}
		}
		
		game();
		
	}
	
	private static void game() throws java.io.IOException{
		System.out.println("The Coded Text is:- "+output);
		String Ans = br.readLine().toUpperCase();
		System.out.print(coded_txt);
		System.out.print(Ans);
		
		if(Ans == coded_txt) {
			System.out.println("You Are Correct!!!");
		}else if(Ans != coded_txt) {
			System.out.println("Lets Try Again!!");
//			game();
		}
		
	}

}
