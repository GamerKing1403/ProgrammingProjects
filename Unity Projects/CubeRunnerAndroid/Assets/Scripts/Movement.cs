using UnityEngine;
using UnityEngine.UI;

public class Movement : MonoBehaviour
{
    public Rigidbody rb;
    public float forwardForce = 2000f;
    public float sidewaysForce = 500f;
    public Text score;
    public Text result;
    bool hasFallen = false;
    public float speed = 10f;

    // Update is called once per frame
    void FixedUpdate()
    {
        if (Input.touchCount > 0 && Input.GetTouch(0).position.x < Screen.width / 2)
        {
            rb.AddForce(-sidewaysForce * Time.fixedDeltaTime, 0, 0, ForceMode.VelocityChange);
        }
        else if (Input.touchCount > 0 && Input.GetTouch(0).position.x > Screen.width / 2)
        {
            rb.AddForce(sidewaysForce * Time.fixedDeltaTime, 0, 0, ForceMode.VelocityChange);
        }
        //float x = Input.GetAxis("Horizontal") * Time.fixedDeltaTime * speed;

        rb.AddForce(0, 0, forwardForce * Time.fixedDeltaTime);

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
