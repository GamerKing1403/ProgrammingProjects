import java.io.IOException;

interface Greet{
	void greet();
	String name = "Tushar";
}


public class lambdaFunction {

	public static void main(String[] args) throws InterruptedException, IOException {
		Greet g1 = () -> System.out.println("Hello World From "+Greet.name);
		g1.greet();
	}

}
