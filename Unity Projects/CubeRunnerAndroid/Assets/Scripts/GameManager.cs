using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    bool gameHasEnded = false;
    public float waitTime = 2f;
    public GameObject levelEndedUI;
    public Text highScore;

    public void EndGame()
    {
        if (gameHasEnded == false)
        {
            gameHasEnded = true;
            Invoke("Restart", waitTime);
        }
    }
    void Restart()
    {
        levelEndedUI.SetActive(true);
        int highscore = PlayerPrefs.GetInt("highscore", 0);
        highScore.text += highscore.ToString();
    }
}
