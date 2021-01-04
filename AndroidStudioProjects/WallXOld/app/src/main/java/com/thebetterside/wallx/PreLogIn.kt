package com.thebetterside.wallx

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.Button
import android.widget.Spinner

class PreLogIn : AppCompatActivity(), View.OnClickListener, AdapterView.OnItemSelectedListener {

    private var ok: Button? = null
    private var dropDown: Spinner? = null
    private var notification: Boolean = true
    private var conti: Boolean = true
    private var op1: String? = null
    private var op2: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_pre_log_in)

        op1 = getString(R.string.yes)
        op2 = getString(R.string.no)

        ok = findViewById(R.id.ok)
        dropDown = findViewById(R.id.dropDown)

        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, arrayOf(op1, op2))

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
            R.id.ok -> {
                if (conti) {
                    val intent = Intent(this@PreLogIn, MainActivity2::class.java)
                    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK) //This is for a Removing every activity before the one we are changing to
                    intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK)
                    intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION)
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
