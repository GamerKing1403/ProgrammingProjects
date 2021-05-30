package com.example.populationchecker

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button

abstract class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var submit = findViewById<Button>(R.id.submit)
        

    }
    fun changePage(){
        val intent = Intent(this@MainActivity, Activity2::class.java)
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK)
        intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION)
        startActivity(intent) // This start the next activity
        overridePendingTransition(R.anim.slide_in_right, R.anim.slide_out_left)
    }
}