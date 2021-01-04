package com.thebetterside.wallex;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Name extends AppCompatActivity {

    public static String name;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_name);

        Button ok = findViewById(R.id.ok);

        ok.setOnClickListener(
                new Button.OnClickListener(){
                    @Override
                    public void onClick(View v) {
                        EditText nameInput = findViewById(R.id.nameInput);
                        if(nameInput.getText().toString().equals("")){
                            Toast.makeText(Name.this, "Please Enter A Name", Toast.LENGTH_SHORT).show();
                        }else{
                            name = nameInput.getText().toString();
                            Intent intent = new Intent(Name.this, MainActivity2.class);
                            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                            intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
                            intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION);
                            startActivity(intent);
                            overridePendingTransition(R.anim.slide_in_right,R.anim.slide_out_left);
                        }
                    }
                }
        );
    }

    @Override
    public void finish() {
        super.finish();
        overridePendingTransition(R.anim.slide_in_left, R.anim.slide_out_right);
    }
}
