using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class start : MonoBehaviour
{
    public Text highScore;
    public GameObject mainMenu;
    public GameObject controls;

    public void Controls()
    {
        mainMenu.SetActive(false);
        controls.SetActive(true);
    }

    public void Return()
    {
        mainMenu.SetActive(true);
        controls.SetActive(false);
    }

    void Start()
    {
        highScore.text += PlayerPrefs.GetInt("highscore", 0);
    }

    public void Quit()
    {
        Application.Quit();
    }
    public void initiate()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }
}
