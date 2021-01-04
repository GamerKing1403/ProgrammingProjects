package com.thebetterside.wallex;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.os.SystemClock;
import android.widget.ProgressBar;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

import org.jetbrains.annotations.NotNull;

public class MainActivity extends AppCompatActivity {
    private Handler mHandler = new Handler();
    private int progress = 0;
    private Context context;
    private ProgressBar progressBar;
    private Thread t1;
    private String[] path = {"wallex1.jpg", "wallex2.jpg", "wallex3.jpg", "wallex4.jpg", "wallex5.jpg"};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        context = this;
        progressBar = findViewById(R.id.progressBar);

        t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                fireBasePreLoader(path);
            }
        });
        t1.start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                while(progress < 100) {
                    progress++;
                    SystemClock.sleep(25);
                    try {
                        t1.join();
                    } catch (InterruptedException e) {
                        Toast.makeText(context, "An Error Occurred", Toast.LENGTH_SHORT);
                    }
                    mHandler.post(new Runnable() {
                        @Override
                        public void run() {
                            progressBar.setProgress(progress);
                        }
                    });
                }
                mHandler.post(new Runnable() {
                    @Override
                    public void run() {
                        opening();
                    }
                });
            }
        }).start(); //This is the Progress Bar
    }

    public String fireBasePathCreator(String path){
        return "https://firebasestorage.googleapis.com/v0/b/wallex-1403.appspot.com/o/" + path + "?alt=media";
    }// This is the method for creating the path for FireBase images

    public void fireBasePreLoader(@NotNull String[] path){
        for (String s : path) {
            Glide
                    .with(context)
                    .load(fireBasePathCreator(s))
                    .preload();
        }
    } // This is for PreLoading those images

    public void opening(){
        final String PREFS_NAME = "MyPrefsFile";
        SharedPreferences settings = getSharedPreferences(PREFS_NAME, 0);

        if (settings.getBoolean("my_first_time", true)) {
            Intent intent = new Intent(MainActivity.this, OnBoarding.class);
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
            intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION);
            startActivity(intent); // This start the next activity
            settings.edit().putBoolean("my_first_time", false).apply();
        } else {
            Intent intent = new Intent(MainActivity.this, MainActivity2.class);
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);   //This is for a Removing every activity before the one we are changing to
            intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
            intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION);
            startActivity(intent);// This start the next activity
        }
    } // This is used to make the open different page when the app is installed and when it is open the second time

}