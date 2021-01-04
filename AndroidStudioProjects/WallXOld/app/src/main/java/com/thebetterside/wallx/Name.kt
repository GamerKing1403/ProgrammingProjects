package com.thebetterside.wallx

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class Name : AppCompatActivity(), View.OnClickListener {

    var name: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_name)
        val ok = findViewById<Button>(R.id.ok)
        ok.setOnClickListener(this)

    }

    override fun onClick(v: View?) {
        when(v!!.id){
            R.id.ok -> {
                val nameInput = findViewById<EditText>(R.id.nameInput)
                if (nameInput.text.toString() == "") {
                    Toast.makeText(this@Name, "Please Enter A Name", Toast.LENGTH_SHORT).show()
                } else {
                    name = nameInput.text.toString()
                    val intent = Intent(this@Name, QualityOnBoarding::class.java)
                    startActivity(intent)
                    overridePendingTransition(R.anim.slide_in_right, R.anim.slide_out_left)
                }
            }
        }
    }

    override fun finish() {
        super.finish()
        overridePendingTransition(R.anim.slide_in_left, R.anim.slide_out_right)
    }
}
