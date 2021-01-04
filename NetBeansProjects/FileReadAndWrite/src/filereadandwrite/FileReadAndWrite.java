package filereadandwrite;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FileReadAndWrite {

    public static void main(String[] args) throws InterruptedException, IOException{
        timeChecker();
    }
    public static void timeChecker() throws InterruptedException, IOException{
        Date date = new Date();
        SimpleDateFormat timeFormat = new SimpleDateFormat("HH:mm:ss");
        String time = timeFormat.format(date);
        System.out.println(time);
        Thread.sleep(1000);
        if(time.equals("19:27:00")){
            System.out.println("Done");
        }else{
            timeChecker();
        }
    }
}