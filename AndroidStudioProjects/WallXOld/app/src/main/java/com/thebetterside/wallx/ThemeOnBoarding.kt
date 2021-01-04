package com.thebetterside.wallx

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.Spinner

class ThemeOnBoarding : AppCompatActivity(), View.OnClickListener, AdapterView.OnItemSelectedListener {

    private var ok: Button? = null
    private var dropDown: Spinner? = null
    private var conti: Boolean = true
    private var op1: String? = null
    private var op2: String? = null
    private var op3: String? = null
    private var mode: Int = -1

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_theme)

        op1 = getString(R.string.sysDecide)
        op2 = getString(R.string.dark)
        op3 = getString(R.string.light)

        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, arrayOf(op1, op2, op3))

        ok = findViewById(R.id.ok)
        dropDown = findViewById(R.id.dropDown)

        dropDown!!.adapter = adapter

        ok!!.setOnClickListener(this)
    }

    override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        when(parent!!.getItemAtPosition(position)){
            op1 -> mode = 0
            op2 -> mode = 1
            op3 -> mode = 2
        }
    }

    override fun onNothingSelected(parent: AdapterView<*>?) {
        conti = false
    }

    override fun onClick(v: View?) {
        when(v!!.id){
            R.id.ok -> {
                if (conti){
                    val pref = applicationContext.getSharedPreferences("MyPref", 0) // 0 - for private mode
                    val editor: SharedPreferences.Editor = pref.edit()
                    editor.putInt("quality", mode)
                    editor.apply()
                    val intent = Intent(this@ThemeOnBoarding, PreLogIn::class.java)
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
