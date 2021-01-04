using UnityEngine;
using UnityEngine.UI;

public class PlayerCollision : MonoBehaviour
{
    public Movement playerMovement;
    public Text score;
    public Text result;
    public GameObject musicControler;
    bool collidedOrNot = false;
    private void OnCollisionEnter(Collision collisionInfo)
    {
        if(collisionInfo.collider.CompareTag("Obstacle") && !collidedOrNot)
        {
            playerMovement.enabled = false;
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
            musicControler.SetActive(false);
        }
    }
}
