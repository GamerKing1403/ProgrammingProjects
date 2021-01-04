package com.example.myapplication100;

import androidx.appcompat.app.AppCompatActivity;
import android.widget.Button;
import android.widget.EditText;
import android.view.*;
import android.widget.Switch;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(final Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final Button button = findViewById(R.id.button);
        final EditText editText = findViewById(R.id.editText);
        final EditText editText2 = findViewById(R.id.editText2);
        final EditText editText3 = findViewById(R.id.editText3);
        final EditText editText4 = findViewById(R.id.editText4);
        final Switch switch1 = findViewById(R.id.switch1);
        final Button button2 = findViewById(R.id.button2);
        button.setOnClickListener(
            new Button.OnClickListener(){
                public void onClick(View v){
                    setContentView(R.layout.actvity2);
                    TextView textView5 = findViewById(R.id.textView5);
                    //String Text = ;
                    textView5.setText(
                            "The Password is :- "+ editText.getText()+"\nThe E-mail is :- "+editText2.getText()
                                    +"\nThe Time Is :- "+editText3.getText()+"\nThe Date Is :- "+editText4.getText( )
                    );
                    if (switch1.isChecked()) {
                       textView5.append("\nYou Turned On the Switch");
                    }
                    else{
                        textView5.append("\nYou Didn't Check The switch");
                    }
                    button2.setOnClickListener(
                            new Button.OnClickListener(){
                                public void onClick(View v){
                                    onCreate();
                                }
                            }
                    );

                }
            }
        );
    }
}
