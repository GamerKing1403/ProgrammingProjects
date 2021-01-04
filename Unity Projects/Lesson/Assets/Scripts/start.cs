using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class start : MonoBehaviour
{
    public Text highScore;
    public GameObject mainMenu;

    public void Settings()
    {
        SceneManager.LoadScene(2);
    }

    void Start()
    {
        try
        {
            highScore.text += PlayerPrefs.GetInt("highscore", 0);
        }
        catch (System.NullReferenceException)
        { 
        }
        
    }

    public void initiate()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }
}
