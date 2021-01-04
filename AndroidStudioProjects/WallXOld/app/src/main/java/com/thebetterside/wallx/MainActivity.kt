package com.thebetterside.wallx

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.SystemClock
import android.widget.ProgressBar
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide

class MainActivity : AppCompatActivity() {

    private val mHandler = Handler()
    private var progres = 0
    private var progressBar: ProgressBar? = null
    private val path = arrayOf("wallex1.jpg","wallex2.jpg","wallex3.jpg","wallex4.jpg","wallex5.jpg")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val context: Context = this

        progressBar = findViewById(R.id.progressBar)

        val t1 = Thread(Runnable { fireBasePreLoader(path, context)})

        t1.start()

        Thread(Runnable {
            while (progres < 100) {
                progres += 2
                SystemClock.sleep(25)
                mHandler.post {progressBar!!.progress = progres}
                try {
                    t1.join()
                } catch (e: InterruptedException) {
                    Toast.makeText(context, "An Error Occurred", Toast.LENGTH_SHORT).show()
                }
            }
            mHandler.post {opening()}
        }).start()

    }

    private fun fireBasePathCreator(path: String): String? {
        return "https://firebasestorage.googleapis.com/v0/b/wallex-1403.appspot.com/o/$path?alt=media"
    } // This is the method for creating the path for FireBase images

    private fun fireBasePreLoader(path: Array<String>, context: Context) {
        for (s in path) {
            Glide
                .with(context)
                .load(fireBasePathCreator(s))
                .preload()
        }
    } // This is for PreLoading those images

    private fun opening() {
        val pref = getSharedPreferences("MyPref", 0)
        if (pref.getBoolean("my_first_time", true)) {
            val intent = Intent(this@MainActivity, OnBoarding::class.java)
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK)
            intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION)
            startActivity(intent) // This start the next activity
            overridePendingTransition(R.anim.slide_in_right, R.anim.slide_out_left)
        } else {
            val intent = Intent(this@MainActivity, OnBoarding::class.java)
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK) //This is for a Removing every activity before the one we are changing to
            intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK)
            intent.addFlags(Intent.FLAG_ACTIVITY_NO_ANIMATION)
            startActivity(intent) // This start the next activity
            overridePendingTransition(R.anim.slide_in_right, R.anim.slide_out_left)
        }
    } // This is used to make the open different page when the app is installed and when it is open the second time

}
