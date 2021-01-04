package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.GestureDetectorCompat;

import android.os.Bundle;
import android.widget.*;
import android.view.MotionEvent;
import android.view.GestureDetector;
import android.view.View;

public class MainActivity extends AppCompatActivity implements GestureDetector.OnGestureListener,
GestureDetector.OnDoubleTapListener{

    private TextView text1;
    private GestureDetectorCompat gestureDetector;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        text1 = (TextView)findViewById(R.id.text1);
        this.gestureDetector = new GestureDetectorCompat(this,this);
        gestureDetector.setOnDoubleTapListener(this);

        final Button button1 = (Button)findViewById(R.id.button1);

        final Button button2 = (Button)findViewById(R.id.button2);

        button1.setOnClickListener(
                new Button.OnClickListener(){
                    public void onClick(View v){
                        TextView text1 = (TextView)findViewById(R.id.text1);
                        text1.setText("Good Job Dracie");
                        button1.setText("Try Long Pressing Me");
                    }
                }
        );


        button1.setOnLongClickListener(
                new Button.OnLongClickListener(){
                    public boolean onLongClick(View v){
                        TextView text1 = (TextView)findViewById(R.id.text1);
                        text1.setText("Hello Dracie. Try Scrolling And Other Gestures");
                        button1.setText("Press Me");
                        return true;
                    }
                }
        );

        button2.setOnClickListener(
                new Button.OnClickListener(){
                    public void onClick(View v){
                        TextView text1 = (TextView)findViewById(R.id.text1);
                        text1.setText("Hello");
                        button1.setText("Press Me");
                    }
                }
        );
    }

    @Override
    public boolean onSingleTapConfirmed(MotionEvent motionEvent) {
        text1.setText("Single Tap");
        return true;
    }

    @Override
    public boolean onDoubleTap(MotionEvent motionEvent) {
        text1.setText("Double Tap");
        return true;
    }

    @Override
    public boolean onDoubleTapEvent(MotionEvent motionEvent) {
        text1.setText("Double Tap");
        return true;
    }

    @Override
    public boolean onDown(MotionEvent motionEvent) {
        text1.setText("Swipe");
        return true;
    }

    @Override
    public void onShowPress(MotionEvent motionEvent) {
        text1.setText("Press");

    }

    @Override
    public boolean onSingleTapUp(MotionEvent motionEvent) {
        text1.setText("Single Tap Up");
        return true;
    }

    @Override
    public boolean onScroll(MotionEvent motionEvent, MotionEvent motionEvent1, float v, float v1) {
        text1.setText("Scroll");
        return true;
    }

    @Override
    public void onLongPress(MotionEvent motionEvent) {
        text1.setText("Long Press");
    }

    @Override
    public boolean onFling(MotionEvent motionEvent, MotionEvent motionEvent1, float v, float v1) {
        text1.setText("Fling");
        return true;
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        this.gestureDetector.onTouchEvent(event);
        return super.onTouchEvent(event);
    }
}