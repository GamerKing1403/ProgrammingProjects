using UnityEngine;

public class FollowPlayer : MonoBehaviour
{
    public Vector3 offset;
    // Update is called once per frame
    void Update()
    {
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        transform.position = player.transform.position + offset;
    }
}
