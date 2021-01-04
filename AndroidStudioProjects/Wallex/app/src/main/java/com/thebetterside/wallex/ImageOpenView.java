package com.thebetterside.wallex;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.widget.ImageView;

import com.bumptech.glide.Glide;

public class ImageOpenView extends AppCompatActivity {

    String path = MainActivity2.sharedPath;
    Context context;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_image_open_view);
        context = this;

        ImageView img = findViewById(R.id.BackgroundImage);

        Glide
                .with(context)
                .load(path)
                .fitCenter()
                .onlyRetrieveFromCache(true)
                .into(img);
    }

    public void finish() {
        super.finish();
        overridePendingTransition(R.anim.slide_in_left, R.anim.slide_out_right);
    } //Closing animation
}
