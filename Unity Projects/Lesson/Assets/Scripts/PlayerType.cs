using UnityEngine;

public class PlayerType : MonoBehaviour
{
    void Start()
    {
        GameObject player = GameObject.FindWithTag("Player");
        BoxCollider boxCollider = player.GetComponent<BoxCollider>();
        CapsuleCollider capsuleCollider = player.GetComponent<CapsuleCollider>();
        SphereCollider sphereCollider = player.GetComponent<SphereCollider>();
        switch (PlayerPrefs.GetString("Type", "Cube"))
        {
            case "Cube":
                boxCollider.enabled = true;
                capsuleCollider.enabled = false;
                sphereCollider.enabled = false;
                break;
            case "Capsule":
                boxCollider.enabled = false;
                capsuleCollider.enabled = true;
                sphereCollider.enabled = false;
                break;
            case "Sphere":
                boxCollider.enabled = false;
                capsuleCollider.enabled = false;
                sphereCollider.enabled = true;
                break;
            case "Cylinder":
                boxCollider.enabled = false;
                capsuleCollider.enabled = true;
                sphereCollider.enabled = false;
                break;
            default:
                break;
        }
    }
}
