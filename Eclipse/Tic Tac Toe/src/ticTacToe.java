import java.io.IOException;

public class ticTacToe{

	static char[][] gameBoard = {{' ', '|', ' ', '|', ' '},
			{'-', '+', '-', '+', '-'},
			{' ', '|', ' ', '|', ' '},
			{'-', '+', '-', '+', '-'},
			{' ', '|', ' ', '|', ' '}};
	
	public static void main(String[] args) throws InterruptedException, IOException {
		for(char[] row : gameBoard) {
			for(char c : row) {
				System.out.print(c);
			}
			System.out.println();
		}
		new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
	}
	public static void clearScreen() {
		System.out.print("\033[H\033[2J");
		System.out.flush();
	}

}
