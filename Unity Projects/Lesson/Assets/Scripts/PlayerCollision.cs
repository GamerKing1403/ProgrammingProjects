using System;
using UnityEngine;
using UnityEngine.UI;

public class PlayerCollision : MonoBehaviour
{
    public bool collidedOrNot = false;
    public Text result;
    private void OnCollisionEnter(Collision collisionInfo)
    {
        Movement playerMovement = gameObject.GetComponent<Movement>();
        Text score = GameObject.FindWithTag("Score").GetComponent<Text>();
        GameObject musicControler = GameObject.FindWithTag("Music");
        if(collisionInfo.collider.CompareTag("Obstacle") && !collidedOrNot)
        {
            Stop(playerMovement);
            FindObjectOfType<GameManager>().EndGame();
            FindObjectOfType<ObstacleSpawner>().collisionDetector = true;
            FindObjectOfType<Score>().collisionDetector = true;
            int currentScore = int.Parse(score.text);
            if (PlayerPrefs.GetInt("highscore",0) < currentScore)
            {
                PlayerPrefs.SetInt("highscore", int.Parse(score.text));
            }
            result.text += currentScore;
            collidedOrNot = true;
            if (PlayerPrefs.GetInt("Music", -1) == 1)
            {
                musicControler.SetActive(false);
            }
        }
    }

    private void Stop(Movement playerMovement)
    {
        gameObject.GetComponent<Rigidbody>().AddForce(0, 0, - (playerMovement.forwardForce * Time.fixedDeltaTime));
    }
}
