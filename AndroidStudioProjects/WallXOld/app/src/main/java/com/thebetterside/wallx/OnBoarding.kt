package com.thebetterside.wallx

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class OnBoarding : AppCompatActivity() {

    private var intent1: Intent? = null
    private var exit = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_on_boarding)
        val go = findViewById<Button>(R.id.go)
        go.setOnClickListener {
            intent1 = Intent(this@OnBoarding, Name::class.java)
            startActivity(intent1)
            overridePendingTransition(R.anim.slide_in_right, R.anim.slide_out_left)
        }
    }

    override fun onBackPressed() {
        if (exit) {
            finish() // finish activity
        } else {
            Toast.makeText(
                this, "Press Back again to Exit.",
                Toast.LENGTH_SHORT
            ).show()
            exit = true
            Handler().postDelayed({ exit = false }, 3 * 1000.toLong())
        }
    } // Used to close the app when back button is pressed twice


}
