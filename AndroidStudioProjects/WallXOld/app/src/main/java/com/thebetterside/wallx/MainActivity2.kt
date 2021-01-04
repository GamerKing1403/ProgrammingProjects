package com.thebetterside.wallx

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.content.SharedPreferences.Editor
import android.os.Bundle
import android.os.Handler
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide
import java.util.*

class MainActivity2 : AppCompatActivity(),View.OnClickListener{

    private var context: Context? = null
    private var exit = false
    private val paths: Array<String> = arrayOf("wallex1.jpg","wallex2.jpg","wallex3.jpg","wallex4.jpg","wallex5.jpg","wallex1.jpg","wallex2.jpg","wallex3.jpg","wallex4.jpg","wallex5.jpg")
    private var imgs = ArrayList<ImageView>()
    private val imgViewIds: Array<Int> = arrayOf(R.id.img1,R.id.img2,R.id.img3,R.id.img4,R.id.img5, R.id.likedImg1, R.id.likedImg2, R.id.likedImg3, R.id.likedImg4, R.id.likedImg5)
    private var name: String? = null
    private var likedSec: TextView? = null
    private var likedScrollView: HorizontalScrollView? = null
    private var pref: SharedPreferences? = null
    private var name2: String? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main2)

        context = this

        pref = getSharedPreferences("MyPref", 0)
        pref!!.edit().putBoolean("my_first_time", false).apply()
        init()

        name2 = pref!!.getString("name2", "")

        load(imgs, paths)
    }

    private fun init(){
        likedSec = findViewById(R.id.likedSec)
        likedScrollView = findViewById(R.id.likedScrollView)
        for (i in imgViewIds.indices ){
            imgs.add(findViewById(imgViewIds[i]))
        }

        for(i in imgs.indices){
            imgs[i].setOnClickListener(this)
        }
    }

    override fun onClick(v: View) {
        imgClick(v.id)
    } // All of the Onclick Functions in One Place

    private fun imgClick(res: Int){
        val intent = Intent(context, ImageOpenView::class.java)
        val editor: Editor = pref!!.edit()
        name = findViewById<ImageView>(res).contentDescription.toString()
        editor.putString("link", fireBasePathCreator(name!!))
        editor.putString("name", name)
        editor.apply()
        startActivity(intent)
        overridePendingTransition(R.anim.slide_in_right, R.anim.slide_out_left)
    }

    private fun fireBasePathCreator(path: String): String? {
        return "https://firebasestorage.googleapis.com/v0/b/wallex-1403.appspot.com/o/$path?alt=media"
    } // creates a Path for an image from FireBase

    private fun load(imgs: ArrayList<ImageView>, paths: Array<String>) {
        for (i in imgs.indices) {
            Glide
                .with(context!!)
                .load(fireBasePathCreator(paths[i]))
                .onlyRetrieveFromCache(true)
                .placeholder(R.drawable.no_internet)
                .error(R.drawable.no_internet)
                .into(imgs[i])

            imgs[i].contentDescription = paths[i]
        }

    } // Loads the image from the given Path into the Given imageViews

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

    override fun finish() {
        super.finish()
        overridePendingTransition(R.anim.slide_in_left, R.anim.slide_out_right)
    } //Closing animation

}
