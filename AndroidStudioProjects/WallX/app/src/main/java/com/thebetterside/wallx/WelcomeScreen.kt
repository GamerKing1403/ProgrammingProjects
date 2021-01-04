package com.thebetterside.wallx

import android.graphics.Typeface
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class WelcomeScreen : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.welcome_scr)
        var welcome:TextView = findViewById(R.id.welcome)
//        val font: Typeface = Typeface.createFromFile("font/josefinsans_bold.ttf")
    }
}
