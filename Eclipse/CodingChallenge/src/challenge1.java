import java.util.Scanner;

public class challenge1 {

	private static final Scanner sc = new Scanner(System.in);
	private static int number_of_iterations,x1,y1,x2,y2,v1,v2;
	private static float time = 0f;
	
	public static void main(String[] args) {

		number_of_iterations = sc.nextInt();
		
		for(int i = 0; i < number_of_iterations; i++) {
			
			x1 = sc.nextInt();
			y1 = sc.nextInt();
			x2 = sc.nextInt();
			y2 = sc.nextInt();
			v1 = sc.nextInt();
			v2 = sc.nextInt();
			
		    if(x1 == x2) {
				time -= ((float)y1)/v1;
				time += ((float)y2)/v2;
    		}else {
    		    if(y1 < 0 && y2 > 0){
    		        float x = (((float)(x1 - x2)*y1)/(y2-y1)) + x1;
    		        int x3 = round(x);
    				time += (float)(sqrt(pow(x3 - x1, 2) + pow(y1, 2)))/v1;
    				time += (float)(sqrt(pow(x2 - x3, 2) + pow(y2, 2)))/v2;
    		    }else if (y1 > 0 && y2 > 0 ){
    				time += ((float)(sqrt(pow(x1 - x2, 2) + pow(y1-y2, 2))))/v2;
    		    }
    		}
		    
		    String Time = String.format("%.5f", time);
        		
			System.out.println(Time);
		}
	}
    
    private static float sqrt(float no){
        return (float)Math.sqrt(no);
    }
    
    private static float pow(float no, float pow){
        return (float)Math.pow(no, pow);
    }
    
    private static int round(float no){
        return Math.round(no);
    }
}