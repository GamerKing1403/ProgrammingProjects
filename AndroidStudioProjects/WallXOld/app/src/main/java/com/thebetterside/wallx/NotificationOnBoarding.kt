package com.thebetterside.wallx

import android.content.Intent
import android.content.SharedPreferences
import android.content.SharedPreferences.Editor
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.Spinner
import androidx.appcompat.app.AppCompatActivity


class NotificationOnBoarding : AppCompatActivity(), View.OnClickListener, AdapterView.OnItemSelectedListener {

    private var ok: Button? = null
    private var dropDown: Spinner? = null
    private var notification: Boolean = true
    private var conti: Boolean = true
    private var op1: String? = null
    private var op2: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_notification_on_boarding)

        op1 = getString(R.string.yes)
        op2 = getString(R.string.no)

        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, arrayOf(op1, op2))

        ok = findViewById(R.id.ok)
        dropDown = findViewById(R.id.dropDown)

        dropDown!!.adapter = adapter
        ok!!.setOnClickListener(this)

    }

    override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        if(parent!!.getItemAtPosition(position) == op2){
            notification = false
        }
    }

    override fun onNothingSelected(parent: AdapterView<*>?) {
        conti = false
    }

    override fun onClick(v: View?) {
        when(v!!.id){
            R.id.ok ->{
                if (conti) {
                    val pref = applicationContext.getSharedPreferences("MyPref", 0) // 0 - for private mode
                    val editor: Editor = pref.edit()
                    editor.putBoolean("notification", notification)
                    editor.apply()
                    val intent = Intent(this@NotificationOnBoarding, ThemeOnBoarding::class.java)
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
