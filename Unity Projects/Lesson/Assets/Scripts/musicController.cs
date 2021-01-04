using UnityEngine;

public class musicController : MonoBehaviour
{
    public GameObject musicControler;
    void Start()
    {
        if (PlayerPrefs.GetInt("Music", 1) == 1)
        {
            musicControler.SetActive(true);
        }
        else
        {
            musicControler.SetActive(false);
        }
    }
}
