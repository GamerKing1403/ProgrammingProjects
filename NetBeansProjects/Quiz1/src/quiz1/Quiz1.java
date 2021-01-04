package quiz1;
import java.util.Scanner;
public class Quiz1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        char ch = 'Y';
        while(ch == 'Y'|| ch == 'y'){
            System.out.println();
            ques1();
            System.out.println();
            String ans1 = scan.next();
            int score = ans1(ans1);
            System.out.println();
            ques2();
            String ans2 = scan.next();
            score += ans2(ans2);
            System.out.println();
            ques3();
            String ans3 = scan.next();
            score += ans3(ans3);
            System.out.println("Your Score Is :- " + score);
            switch (score) {
                case 30:System.out.println("Very Good You Have Answered All Answer Correctly!!!");break;
                case 10:case 20:System.out.println("Good But You Have Answered Only One or Two Answer Correctly!!!");break;
                case 0:System.out.println("Bad You Have Answered All The Answers Wrong You Need To Learn G.K.");break;
                default:break;
            }
            System.out.println("Do You Want To Continue ?(Y for Yes And N for No)");
            ch = scan.next().charAt(0);
        }
        scan.close();
    }
    public static void ques1(){
        System.out.println("Q1) Which Of These Is Not A Browser ?");
        System.out.println("A) Facebook");
        System.out.println("B) Chrome");
        System.out.println("C) Firefox");
        System.out.println("D) Opera");
        System.out.println("What Is The Answer ?");
    }
    public static int ans1(String a){
        int score = 0;
        switch(a){
            case "A":case "a":score = 10;break;
            case "B":case "b":break;
            case "C":case "c":break;
            case "D":case "d":break;
            default:System.out.println("You Have Done Something Wrong");break;
        }
        return score;
    }
    public static void ques2(){
        System.out.println("Q2) Who Is The CEO Of Google ?");
        System.out.println("A) Mark Zuckerburg");
        System.out.println("B) Sunder Pichai");
        System.out.println("C) Tim Cook");
        System.out.println("D) Bill Gates");
        System.out.println("What Is The Answer ?");
    }
    public static int ans2(String a){
        int score = 0;
        switch(a){
            case "A":case "a":break;
            case "B":case "b":score = 10;break;
            case "C":case "c":break;
            case "D":case "d":break;
            default:System.out.println("You Have Done Something Wrong");break;
        }
        return score;
    }
    public static void ques3(){
        System.out.println("Q3) What is The Name Of the New Operating System Made By Google ?");
        System.out.println("A) Flutter");
        System.out.println("B) SailFish");
        System.out.println("C) Fuchsia");
        System.out.println("D) Tizen");
        System.out.println("What Is The Answer ?");
    }
    public static int ans3(String a){
        int score = 0;
        switch(a){
            case "A":case "a":break;
            case "B":case "b":break;
            case "C":case "c":score = 10;break;
            case "D":case "d":break;
            default:System.out.println("You Have Done Something Wrong");break;
        }
        return score;
    }
}