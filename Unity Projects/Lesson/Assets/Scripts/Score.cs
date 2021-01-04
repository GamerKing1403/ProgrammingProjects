using UnityEngine.UI;
using UnityEngine;

public class Score : MonoBehaviour
{
    public Text scoreText;
    public bool collisionDetector = false;

    // Update is called once per frame
    void Update()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (collisionDetector == false)
        {
            scoreText.text = player.transform.position.z.ToString("0");
        }
        
    }
}
