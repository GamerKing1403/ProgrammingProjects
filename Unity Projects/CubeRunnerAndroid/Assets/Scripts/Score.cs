using UnityEngine.UI;
using UnityEngine;

public class Score : MonoBehaviour
{
    public Transform player;
    public Text scoreText;
    public bool collisionDetector = false;

    // Update is called once per frame
    void Update()
    {
        if (collisionDetector == false)
        {
            scoreText.text = player.position.z.ToString("0");
        }
        
    }
}
