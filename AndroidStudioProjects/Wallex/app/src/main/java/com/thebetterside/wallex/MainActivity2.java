package com.thebetterside.wallex;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

import org.jetbrains.annotations.NotNull;

public class MainActivity2 extends AppCompatActivity implements View.OnClickListener {

    private Context context;
    private Boolean exit = false;
    public static String sharedPath;
    private String[] paths = {"wallex1.jpg", "wallex2.jpg", "wallex3.jpg", "wallex4.jpg", "wallex5.jpg"};

    @Override
    protected void onCreate(Bundle savedInstanceState)  {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        context = this;

        final ImageButton[] imgs = {findViewById(R.id.img1), findViewById(R.id.img2),
                findViewById(R.id.img3), findViewById(R.id.img4), findViewById(R.id.img5)};

        imgs[0].setOnClickListener(this);
        imgs[1].setOnClickListener(this);
        imgs[2].setOnClickListener(this);
        imgs[3].setOnClickListener(this);
        imgs[4].setOnClickListener(this);

        load(imgs, paths);

    }

    @Override
    public void onClick(@NotNull View v) {
        Intent intent = new Intent(context, ImageOpenView.class);
        switch (v.getId()){
            case R.id.img1:
                sharedPath = fireBasePathCreator(paths[0]);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_in_right,R.anim.slide_out_left);
            case R.id.img2:
                sharedPath = fireBasePathCreator(paths[1]);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_in_right,R.anim.slide_out_left);
            case R.id.img3:
                sharedPath = fireBasePathCreator(paths[2]);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_in_right,R.anim.slide_out_left);
            case R.id.img4:
                sharedPath = fireBasePathCreator(paths[3]);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_in_right,R.anim.slide_out_left);
            case R.id.img5:
                sharedPath = fireBasePathCreator(paths[4]);
                startActivity(intent);
                overridePendingTransition(R.anim.slide_in_right,R.anim.slide_out_left);
        }
    }// All of the Onclick Functions in One Place

    private String fireBasePathCreator(String path){
        return "https://firebasestorage.googleapis.com/v0/b/wallex-1403.appspot.com/o/" + path + "?alt=media";
    }// creates a Path for an image from FireBase

    public void load(ImageView[] imgs, String[] paths){
        for(int i=0; i < imgs.length; i++){
            Glide
                    .with(context)
                    .load(fireBasePathCreator(paths[i]))
                    .onlyRetrieveFromCache(true)
                    .into(imgs[i]);
        }

    } // Loads the image from the given Path into the Given imageViews

    @Override
    public void onBackPressed() {
        if (exit) {
            finish(); // finish activity
        } else {
            Toast.makeText(this, "Press Back again to Exit.",
                    Toast.LENGTH_SHORT).show();
            exit = true;
            new Handler().postDelayed(new Runnable() {
                @Override
                public void run() {
                    exit = false;
                }
            }, 3 * 1000);

        }

    } // Used to close the app when back button is pressed twice

    @Override
    public void finish() {
        super.finish();
        overridePendingTransition(R.anim.slide_in_left, R.anim.slide_out_right);
    } //Closing animation
}
