using UnityEngine.SceneManagement;
using UnityEngine;

public class Retry : MonoBehaviour
{
    public void Restart()
    {
        SceneManager.LoadScene(1);
    }
    public void Quit()
    {
        Application.Quit();
    }

    public void Return()
    {
        SceneManager.LoadScene(0);
    }
}
