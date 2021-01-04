package com.thebetterside.wallx

import android.content.Intent
import android.content.SharedPreferences
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.Spinner
import androidx.appcompat.app.AppCompatActivity


class QualityOnBoarding : AppCompatActivity(), View.OnClickListener, AdapterView.OnItemSelectedListener {
    private var ok: Button? = null
    private var dropDown: Spinner? = null
    private var conti: Boolean = true
    private var op1: String? = null
    private var op2: String? = null
    private var op3: String? = null
    private var quality: Int = -1

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_quality_on_boarding)

        op1 = getString(R.string.high)
        op2 = getString(R.string.medium)
        op3 = getString(R.string.low)

        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, arrayOf(op1, op2, op3))

        ok= findViewById(R.id.ok)
        dropDown = findViewById(R.id.dropDown)

        dropDown!!.adapter = adapter

        ok!!.setOnClickListener(this)
    }

    override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        when(parent!!.getItemAtPosition(position)){
            op1 -> quality = 0
            op2 -> quality = 1
            op3 -> quality = 2
        }
    }

    override fun onNothingSelected(parent: AdapterView<*>?) {
        conti = false
    }

    override fun onClick(v: View?) {
        when(v!!.id) {
            R.id.ok -> {
                if (conti) {
                    val pref = applicationContext.getSharedPreferences("MyPref", 0) // 0 - for private mode
                    val editor: SharedPreferences.Editor = pref.edit()
                    editor.putInt("quality", quality)
                    editor.apply()
                    val intent = Intent(this@QualityOnBoarding, NotificationOnBoarding::class.java)
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
