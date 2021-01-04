using System;
using UnityEngine;
using UnityEngine.UI;

public class Movement : MonoBehaviour
{
    private Rigidbody rb;
    public float forwardForce = 2000f;
    public float sidewaysForce = 500f;
    
    bool hasFallen = false;
    public float speed = 10f;
    private Text score;
    private Text result;

    // Update is called once per frame
    private void Start()
    {
        score = GameObject.FindWithTag("Score").GetComponent<Text>();
        rb = gameObject.GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        if (!gameObject.GetComponent<PlayerCollision>().collidedOrNot)
        { 
            rb.AddForce(0, 0, forwardForce * Time.fixedDeltaTime);
        }
        try
        {
            result = GameObject.FindWithTag("YourScore").GetComponent<Text>();
        }
        catch (Exception e){}            
        if (Input.touchCount > 0 && Input.GetTouch(0).position.x < Screen.width / 2)
        {
            rb.AddForce(-sidewaysForce * Time.fixedDeltaTime, 0, 0, ForceMode.VelocityChange);
        }
        else if (Input.touchCount > 0 && Input.GetTouch(0).position.x > Screen.width / 2)
        {
            rb.AddForce(sidewaysForce * Time.fixedDeltaTime, 0, 0, ForceMode.VelocityChange);
        }

        if (rb.position.y < -1f && !hasFallen)
        {
            FindObjectOfType<GameManager>().EndGame();
            FindObjectOfType<ObstacleSpawner>().collisionDetector = true;
            FindObjectOfType<Score>().collisionDetector = true;
            int currentScore = int.Parse(score.text);
            if (PlayerPrefs.GetInt("highscore", 0) < currentScore)
            {
                PlayerPrefs.SetInt("highscore", int.Parse(score.text));
            }
            result.text += currentScore;
            hasFallen = true;
        }
    }
}
