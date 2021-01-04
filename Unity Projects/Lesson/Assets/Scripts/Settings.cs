using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Settings : MonoBehaviour
{
    public Toggle music;
    void Start()
    {
        int Music = PlayerPrefs.GetInt("Music", 1);
        if (Music == 1)
        {
            music.isOn = true;
        }
        else
        {
            music.isOn = false;
        }
    }
    public void Return()
    {
        SceneManager.LoadScene(0);
    }
    public void Music(bool musicOffOrOn)
    {
        if (musicOffOrOn)
        {
            PlayerPrefs.SetInt("Music", 1);
        }
        else
        {
            PlayerPrefs.SetInt("Music", 0);
        }
    }
}
