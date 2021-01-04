package com.thebetterside.wallx

import android.Manifest.permission.WRITE_EXTERNAL_STORAGE
import android.app.Dialog
import android.app.DownloadManager
import android.app.WallpaperManager
import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.content.pm.PackageManager
import android.graphics.Color
import android.graphics.drawable.BitmapDrawable
import android.graphics.drawable.ColorDrawable
import android.net.*
import android.os.Build
import android.os.Bundle
import android.os.Environment
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.bumptech.glide.Glide
import com.like.LikeButton
import java.io.IOException


class ImageOpenView : AppCompatActivity(),View.OnClickListener,com.like.OnLikeListener {

    private var mWallpaperManager: WallpaperManager? = null
    private var context: Context? = null
    private var img: ImageView? = null
    private var dialog: Dialog? = null
    private val storagePermissionCodes: Int = 1000
    private var homeOrLock: Int? = null
    private var fragLayout1: View? = null
    private var fragLayout2: View? = null
    private var fadeInOrOut: Boolean = false
    private var liked: Boolean = false
    private var path: String? = null
    private var name: String? = null
    private var homeScr: Button? = null
    private var lockScr: Button? = null
    private var bothHomeLock: Button? = null
    private var download: Button? = null
    private var setWallpaper: Button? = null
    private var back: Button? = null
    private var like: LikeButton? = null
    private var pref:SharedPreferences? = null // 0 - for private mode
    private var editor: SharedPreferences.Editor? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_image_open_view)

        init()
        load()
    }

    private fun load(){
        Glide
            .with(context!!)
            .load(path)
            .centerCrop()
            .onlyRetrieveFromCache(true)
            .into(img!!)
    }

    private fun init(){
        context = this
        pref = applicationContext.getSharedPreferences("MyPref", 0)

        path = pref!!.getString("message", "")
        name = pref!!.getString("name", "")
        liked = pref!!.getBoolean("liked", false)

        mWallpaperManager = WallpaperManager.getInstance(context)

        download = findViewById(R.id.download)
        setWallpaper = findViewById(R.id.setWallpaper)
        back = findViewById(R.id.back)
        img = findViewById(R.id.BackgroundImage)
        like = findViewById(R.id.likeBtn)
        fragLayout1 = findViewById(R.id.layout1)
        fragLayout2 = findViewById(R.id.layout2)
        like!!.isLiked = liked

        dialog = Dialog(context!!)

        like!!.setOnLikeListener(this)
        download!!.setOnClickListener(this)
        setWallpaper!!.setOnClickListener(this)
        back!!.setOnClickListener(this)
        img!!.setOnClickListener(this)
    }

    override fun liked(likeButton: LikeButton?) {
        liked = true
    }

    override fun unLiked(likeButton: LikeButton?) {
        liked = false
    }

    override fun onClick(v: View) {
        when(v.id){
            R.id.download -> {
                download()
            }
            R.id.setWallpaper -> {
                showPopUp()
            }
            R.id.back -> {
                back()
            }
            R.id.homeScr -> {
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
                    homeOrLock = WallpaperManager.FLAG_SYSTEM
                }
                dialog!!.dismiss()
                setWallpaper()
            }
            R.id.lockScr -> {
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
                    homeOrLock = WallpaperManager.FLAG_LOCK
                }
                dialog!!.dismiss()
                setWallpaper()
            }
            R.id.bothHomeLock -> {
                dialog!!.dismiss()
                setWallpaper()
            }
            R.id.BackgroundImage ->{
                if(fadeInOrOut){
                    fadeIn()
                }else{
                    fadeOut()
                }
            }
        }
    }

    private fun fadeOut(){

        fragLayout1!!.animate()
            .translationY(-fragLayout1!!.height.toFloat())
            .alpha(0.0f)
            .duration = 1000

        fragLayout2!!.animate()
            .translationY(fragLayout2!!.height.toFloat())
            .alpha(0.0f)
            .duration = 1000

        fadeInOrOut = true

    }

    private fun fadeIn(){

        fragLayout1!!.animate()
            .translationY(0f)
            .alpha(1.0f)
            .duration = 500

        fragLayout2!!.animate()
            .translationY(0f)
            .alpha(1.0f)
            .duration = 500

        fadeInOrOut = false

    }

    private fun checkNetworkState(context: Context): Boolean? {
        val connectivityManager = context.getSystemService(Context.CONNECTIVITY_SERVICE) as ConnectivityManager
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            val nw = connectivityManager.activeNetwork ?: return false
            val actNw = connectivityManager.getNetworkCapabilities(nw) ?: return false
            return when {
                actNw.hasTransport(NetworkCapabilities.TRANSPORT_WIFI) -> true
                actNw.hasTransport(NetworkCapabilities.TRANSPORT_CELLULAR) -> true
                else -> false
            }
        }
        return null
    }

    private fun download(){
        if (checkNetworkState(this)!!){
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){
                if(checkSelfPermission(WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_DENIED){
                    requestPermissions(arrayOf(WRITE_EXTERNAL_STORAGE), storagePermissionCodes)
                }else{
                    startDownloading()
                }
            }else{
                startDownloading()
            }
        }else{
            Toast.makeText(this, "Internet Not Available", Toast.LENGTH_SHORT).show()
        }

    } //Download Function

    private fun startDownloading() {
        val request = DownloadManager.Request(Uri.parse(path))
        request.setAllowedNetworkTypes(DownloadManager.Request.NETWORK_MOBILE or DownloadManager.Request.NETWORK_WIFI)
        request.setTitle(name)
        request.setDescription("The file is downloading...")

        request.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED)
        request.setDestinationInExternalPublicDir(Environment.DIRECTORY_DOWNLOADS, intent.getStringExtra("name"))

        val manager = getSystemService(Context.DOWNLOAD_SERVICE) as DownloadManager
        manager.enqueue(request)
    } //Starts the download

    override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        when(requestCode){
            storagePermissionCodes -> {
                if( grantResults.isNotEmpty() && grantResults[0] == PackageManager.PERMISSION_GRANTED){
                    startDownloading()
                }else{
                    Toast.makeText(context, "Permission Denied", Toast.LENGTH_SHORT).show()
                }
            }
        }
    }

    private fun showPopUp(){
        dialog!!.setContentView(R.layout.set_resource_layout)

        homeScr = dialog!!.findViewById(R.id.homeScr)
        lockScr = dialog!!.findViewById(R.id.lockScr)
        bothHomeLock = dialog!!.findViewById(R.id.bothHomeLock)

        homeScr!!.setOnClickListener(this)
        lockScr!!.setOnClickListener(this)
        bothHomeLock!!.setOnClickListener(this)

        dialog!!.window!!.setBackgroundDrawable(ColorDrawable(Color.TRANSPARENT))
        dialog!!.show()
    } //PopUp Function.

    private fun setWallpaper(){
        try{
            if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
                if(homeOrLock == null){
                    mWallpaperManager!!.setBitmap((img!!.drawable as BitmapDrawable).bitmap)
                }else{
                    mWallpaperManager!!.setBitmap(
                        (img!!.drawable as BitmapDrawable).bitmap,
                        null,
                        false,
                        homeOrLock!!
                    )
                }
                Toast.makeText(context, "Wallpaper Set!", Toast.LENGTH_SHORT).show()
            }
        }catch (e: IOException){
            Toast.makeText(context, "An Error Occurred", Toast.LENGTH_SHORT).show()
        }
    } //Function to Set The Wallpaper

    private fun back(){
        val intent = Intent(context, MainActivity2::class.java)
        editor = pref!!.edit()
        editor!!.putBoolean("liked", liked)
        editor!!.putString("name2", name)
        editor!!.apply()
        startActivity(intent)
        overridePendingTransition(R.anim.slide_in_left, R.anim.slide_out_right)
    }

    override fun finish() {
        super.finish()
        overridePendingTransition(R.anim.slide_in_left, R.anim.slide_out_right)
    } //Closing animation

}
