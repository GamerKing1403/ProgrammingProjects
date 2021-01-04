import java.util.*;
public class quiz {
    public static void main(String[] args){
       Scanner scan = new Scanner(System.in);
       String ans = scan.nextLine();
       String ans2 = scan.nextLine();
       question1(ans);
       question2(ans2);
       int score = question1(ans) + question2(ans2);
       System.out.println("Your Score Is :- " + score);
    }
    public static int question1(String a){
        System.out.println("Q1) Which Of These Is Not A Browser ?");
        System.out.println("A) Facebook");
        System.out.println("B) Chrome");
        System.out.println("C) Firefox");
        System.out.println("D) Opera");
        //Scanner scan = new Scanner(System.in);
        //String a = scan.nextLine();
        int score = 0;
        switch(a){
            case "A":
                score += 10;
                break;
            case "B":break;
            case "C":break;
            case "D":break;
            default:
                System.out.println("You Have Done Something Wrong");
                break;
        }
        return score;
    }
    public static int question2(String a){
        System.out.println("Q1) Who Is The CEO Of Google ?");
        System.out.println("A) Mark Zuckerburg");
        System.out.println("B) Sunder Pichai");
        System.out.println("C) Tim Cook");
        System.out.println("D) Bill Gates");
        //Scanner scan = new Scanner(System.in);
        //String a = scan.nextLine();
        int score = 0;
        switch(a){
            case "A":break;
            case "B":
                score += 10;
                break;
            case "C":break;
            case "D":break;
            default:
                System.out.println("You Have Done Something Wrong");
                break;
        }
        return score;
    }
    public static int question3(){
        System.out.println("Q1) Which Of These is The New Operating System Getting Devloped By Google?");
        System.out.println("A) Fuchisia");
        System.out.println("B) Flutter");
        System.out.println("C) Sailfish");
        System.out.println("D) Tizen");
        Scanner scan = new Scanner(System.in);
        String a = scan.nextLine();
        int score = 0;
        switch(a){
            case "A":
                score += 10;
                break;
            case "B":break;
            case "C":break;
            case "D":break;
            default:
                System.out.println("You Have Done Something Wrong");
                break;
        }
        return score;
    }
}